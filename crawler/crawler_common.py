import shutil

import requests
from bs4 import BeautifulSoup
from mdutils import MdUtils

from selenium import webdriver

import time

from util import aitools


def crawler_common(url,chromedebugmode=False):

    if chromedebugmode:
        options = webdriver.ChromeOptions()
        options.debugger_address = '127.0.0.1:9222'
        driver = webdriver.Chrome(options=options)
        driver.get(url)

        time.sleep(5)

        # 1、获取所有标签页
        window_handles = driver.window_handles
        driver.switch_to.window(window_handles[0])

        time.sleep(5)

        soup = BeautifulSoup(driver.page_source, "html.parser")
    else:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")

    h1 = soup.h1.string.strip()
    md_file = MdUtils(file_name=h1, title=h1)
    md_file.new_header(level=1, title=h1)
    md_file.new_line(url)

    article = soup.article
    extract(article, md_file)

    md_file.create_md_file()

    shutil.move(h1 + ".md", "posts")


def extract(div, md_file):
    children = div.children
    for child in children:
        if child.name == "div" or child.name == "section":
            extract(child, md_file)
        if child.name == "h1" or child.name == "h2" or child.name == "h3" or child.name == "h4":
            title = child.text.strip()
            translated_title = aitools.translate(title)
            if child.name == "h1":
                md_file.new_header(level=1, title=title)
                md_file.new_header(level=1, title=translated_title)
            if child.name == "h2":
                md_file.new_header(level=2, title=title)
                md_file.new_header(level=2, title=translated_title)
            if child.name == "h3":
                md_file.new_header(level=3, title=title)
                md_file.new_header(level=3, title=translated_title)
            if child.name == "h4":
                md_file.new_header(level=4, title=title)
                md_file.new_header(level=4, title=translated_title)
            print(child.text.strip())
        if child.name == "figure" :
            img = child.find("img")
            img_src = img.get("src")

            markdownImageStr = md_file.new_inline_image("", img_src)
            md_file.new_line(markdownImageStr)
        if child.name == "img":
            img_src = child.get("src")
            markdownImageStr = md_file.new_inline_image("", img_src)
            md_file.new_line(markdownImageStr)
        if child.name == "p":
            phrase = child.text.strip()
            translated_phrase = aitools.translate(phrase)
            md_file.new_paragraph(phrase)
            md_file.new_paragraph(translated_phrase)
        if child.name == "ul":
            lis = child.find_all("li")
            li_text_arr = []
            for li in lis:
                li_text = li.text.strip()
                translated_li_text = aitools.translate(li_text)
                li_text_arr.append(li_text)
                li_text_arr.append(translated_li_text)
            md_file.new_list(li_text_arr)
