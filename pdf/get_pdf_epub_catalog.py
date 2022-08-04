import fitz

# 1: Probability and counting	1
# page num start with zero


extract_desc = [
    {"page_num": 5, "item_start": 1, "item_end": -1},
    {"page_num": 6},
    {"page_num": 7, "item_start": 0, "item_end": 12},
]


def create_catalog_pdf_or_epub(path, extract_desc):
    doc = fitz.open(path)
    entries = []
    for desc in extract_desc:
        page_num_ = desc["page_num"]
        for page in doc.pages(page_num_, page_num_ + 1):
            link_list = page.get_links()[::-1]
            item_start_ = desc.setdefault("item_start", 0)
            item_end_ = desc.setdefault("item_end", len(link_list))
            text_list = page.get_text().split('\n')[item_start_:item_end_]
            # print("%s" % (len(link_list)))
            # print(len(text_list))
            for i in range(0, len(text_list)):
                entries.append(text_list[i] + '\t' + str(link_list[i]["page"]))

    print("\n".join(entries))


create_catalog_pdf_or_epub(
    './Thomas Anderson, Michael Dahlin - Operating Systems_ Principles and Practice, Vol. 1_ Kernels and Processes-Recursive Books (2015).epub',
    extract_desc)

# d = ['a', 'b', 'c', 'd', 'e'].reverse()
# print(d[0:len(d)])

# di = {"a":111}
# print(di["a"])
# print("a" in di)
