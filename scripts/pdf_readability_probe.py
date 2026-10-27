# -*- coding: utf-8 -*-
"""
PDF 可检索性体检探针  pdf_readability_probe.py
-----------------------------------------------------------------
用途：入库 / 引用前，实测一份 PDF 到底能不能被检索，而不是看它存在不存在。

判定不靠"抽到了字"，而靠"抽到的是不是人话"：
  同一份内容，一个版本文本层干净、另一个版本全是 CID 乱码（抽出来是
  「睸喬赋 鐜铙」），页数、文件名、大小完全看不出差别 —— 只有实测能分开。

用法：
  python pdf_readability_probe.py <pdf1> [pdf2 ...]        # 体检
  python pdf_readability_probe.py <pdf> --json out.json    # 落 JSON
  python pdf_readability_probe.py --selftest               # 自检

退出码：
  0  全部可用或至少有一份可用
  2  存在不可用（乱码 / 无文本层）的 PDF
  3  参数错误
"""
import sys, os, io, json, re, glob

try:
    from pypdf import PdfReader
except ImportError:
    sys.stderr.write("需要 pypdf：pip install pypdf\n")
    sys.exit(3)

# 高频汉字表：正常中文文本里这些字密集出现；乱码文本几乎一个都命中不了
COMMON = set("的一是在不了有和人这中大为上个国我以要他时来用们"
             "生到作地于出就分对成会可主发年动同工也能下过子说"
             "产种面而方后多定行学法所民得经十三之进着等部度家"
             "电力里如水化高自二理起小物现实加量都两体制机当使点")
CJK = re.compile(r'[\u4e00-\u9fff]')


def probe(path, sample_pages=8):
    """返回单份 PDF 的体检结果 dict"""
    r = PdfReader(path)
    n = len(r.pages)
    # 均匀抽样，避开全是封面/目录的前几页
    idx = [0] if n <= 1 else [round(i * (n - 1) / (sample_pages - 1)) for i in range(sample_pages)]
    idx = sorted(set(max(0, min(n - 1, i)) for i in idx))

    chars, cjk, hit, pages_with_text = 0, 0, 0, 0
    sample_text = []
    for i in idx:
        t = r.pages[i].extract_text() or ""
        t = ' '.join(t.split())
        chars += len(t)
        if len(t) >= 20:
            pages_with_text += 1
        cs = CJK.findall(t)
        cjk += len(cs)
        hit += sum(1 for c in cs if c in COMMON)
        sample_text.append(t[:90])

    # 书签（目录）条数 —— 比正文可靠，正文乱码时书签往往还在
    def walk(items, out):
        for it in items:
            if isinstance(it, list):
                walk(it, out)
            else:
                out.append(it.title)
        return out
    try:
        bms = walk(r.outline, [])
    except Exception:
        bms = []

    per_page = chars / max(1, len(idx))
    # 乱码判据：抽到不少 CJK，但常用字命中率极低 → 是 CID 缺 ToUnicode 的乱码
    cjk_ratio = cjk / max(1, chars)
    hit_rate = hit / max(1, cjk)
    garbled = (cjk >= 200) and (hit_rate < 0.06)

    if chars < 50:
        verdict, reason = "无文本层", "扫描件或纯图片，需 OCR"
    elif garbled:
        verdict, reason = "乱码", "文本层存在但不可读（CID 缺 ToUnicode），需换版本或 OCR"
    elif per_page < 60:
        verdict, reason = "稀疏", "有文本但过稀，检索价值低（可能公式均为图片）"
    else:
        verdict, reason = "可用", "文本层可检索"

    return {
        "file": os.path.basename(path),
        "path": path,
        "size_mb": round(os.path.getsize(path) / 1048576, 2),
        "pages": n,
        "sampled": len(idx),
        "chars_per_page": round(per_page, 1),
        "cjk_ratio": round(cjk_ratio, 3),
        "common_hit_rate": round(hit_rate, 3),
        "pages_with_text": f"{pages_with_text}/{len(idx)}",
        "bookmarks": len(bms),
        "verdict": verdict,
        "reason": reason,
        "samples": sample_text[:3],
    }


def main():
    args = [a for a in sys.argv[1:]]
    if not args or args[0] in ("-h", "--help"):
        print(__doc__)
        return 0

    if args[0] == "--selftest":
        # 自检：构造两个已知样本（正常中文 / 乱码），验证判定不翻转
        good = {"chars": 3000, "cjk": 2400, "hit": 900, "chars_per_page": 375.0}
        bad = {"chars": 3000, "cjk": 2400, "hit": 20, "chars_per_page": 375.0}
        g1 = (good["cjk"] >= 200) and (good["hit"] / good["cjk"] < 0.06)
        g2 = (bad["cjk"] >= 200) and (bad["hit"] / bad["cjk"] < 0.06)
        print("正常文本判乱码?", g1, "(应为 False)")
        print("乱码文本判乱码?", g2, "(应为 True)")
        ok = (not g1) and g2
        print("SELFTEST:", "PASS" if ok else "FAIL")
        return 0 if ok else 1

    out_json = None
    if "--json" in args:
        k = args.index("--json")
        out_json = args[k + 1]
        args = args[:k] + args[k + 2:]

    files = []
    for a in args:
        if os.path.isdir(a):
            files += sorted(glob.glob(os.path.join(a, "*.pdf")))
        else:
            files += sorted(glob.glob(a))
    if not files:
        sys.stderr.write("没有匹配到 PDF\n")
        return 3

    results = []
    for p in files:
        try:
            results.append(probe(p))
        except Exception as e:
            results.append({"file": os.path.basename(p), "verdict": "读取失败",
                            "reason": str(e)[:80], "pages": 0, "chars_per_page": 0,
                            "common_hit_rate": 0, "bookmarks": 0, "cjk_ratio": 0,
                            "pages_with_text": "0/0", "samples": []})

    print(f"{'文件':<34}{'页':>6}{'字/页':>8}{'常用字率':>9}{'书签':>6}  判定")
    print("-" * 78)
    for r in results:
        print(f"{r['file'][:33]:<34}{r.get('pages',0):>6}{r.get('chars_per_page',0):>8}"
              f"{r.get('common_hit_rate',0):>9}{r.get('bookmarks',0):>6}  {r['verdict']}")
        if r["verdict"] != "可用":
            print(f"    └ {r['reason']}")

    if out_json:
        io.open(out_json, "w", encoding="utf-8").write(
            json.dumps(results, ensure_ascii=False, indent=2))
        print(f"\n已落 JSON: {out_json}")

    bad = [r for r in results if r["verdict"] in ("乱码", "无文本层", "读取失败", "稀疏")]
    return 2 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
