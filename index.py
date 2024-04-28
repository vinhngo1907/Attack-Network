from requests_html import HTMLSession
import csv
import numpy as np
import pandas as pd

session = HTMLSession()
r = session.get("https://tiki.vn/")
r.encoding = "utf-8"

data = []
link_category_dict = dict()


def parse_link(href, currentPage=1, maxPages=1):
    # Check if href already starts with 'https://'
    if href.startswith("https://"):
        page = href + f"?page={currentPage}"
    else:
        base_url = "https://tiki.vn"
        page = f"{base_url}{href}?page={currentPage}"

    # print("page", page)
    _session = HTMLSession()
    _r = _session.get(page)
    items = _r.html.find("div.ProductList__NewWrapper-sc-1dl80l2-0.jXFjHV")

    if len(items) == 0 or currentPage > maxPages:
        return
    for item in items:
        category = link_category_dict[href]
        data.append([item.text.strip().rstrip("."), category])
    nextPage = currentPage + 1

    try:
        print("page ", page)
        parse_link(href, currentPage=nextPage, maxPages=maxPages)
    except Exception as e:
        print("some errors occured when parsing link", str(e))


def get_categories():
    try:
        categories = []
        item_list = r.html.find("div.styles__StyledItemV2-sc-oho8ay-1.bHIPhv")
        for item in item_list:
            href = item.find("a", first=True).attrs["href"]
            category = item.text
            categories.append((href, category))
            link_category_dict[href] = category
        return categories
    except Exception as e:
        print("some errors occured when getting categories", str(e))


def crawl_data():
    try:
        category_tuples = get_categories()
        for category_tuple in category_tuples:
            (href, category_name) = category_tuple
            parse_link(href)
    except Exception as e:
        print("some errors occured when crawling data", str(e))


def save_data():
    print("??????", data)
    try:
        np.random.shuffle(data)
        if len(data) != 0:
            df = pd.DataFrame(data, columns=["product_title", "category"])
            df.to_csv("product.csv", index=False, encoding="utf-8")
            # with open('product.csv', 'w', newline='', encoding='utf-8') as file:
            # writer = csv.writer(file)
            # writer.writerow(["product_title", "category"])
            # for item in data:
            # writer.writerow(item)
    except Exception as e:
        print("some errors occured when saving data", str(e))


category_tutples = get_categories()


def run():
    print("Start crawling")
    crawl_data()
    save_data()


run()
