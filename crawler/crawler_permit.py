import requests
from bs4 import BeautifulSoup
from util import translate
from mdutils import MdUtils

prefix_url = "https://www.permit.io/"
URL = "https://www.permit.io/blog/differences-between-oauth-vs-jwt?ref=dailydev"

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

article = soup.article
print(article.h1.string)
h1 = article.h1.string
mdFile = MdUtils(file_name=h1, title=h1)
translatedH1String = translate.translate(h1)
mdFile.new_header(level=1, title=translatedH1String)

container = article.find_all("div", class_="container")[1]
# print(container)

content = container.css.select_one("div:nth-child(3)")
# print(content)

children = content.children

for child in children:
    tagName = child.name
    # print(child.name)
    if tagName == "h2":
        h2String = child.string
        mdFile.new_header(level=2, title=h2String)
        translatedH2String = translate.translate(h2String)
        mdFile.new_header(level=2, title=translatedH2String)
        print(translatedH2String, end='\n')
    if tagName == "p":
        contentsInPTag = child.children
        completeString = ""
        # p中包含加粗的信息，因此要通过列表来拼接全部内容
        for content in contentsInPTag:
            completeString = completeString + content.string
        mdFile.new_paragraph(completeString)
        translatedCompleteString = translate.translate(completeString)
        mdFile.new_paragraph(translatedCompleteString)
        print(completeString)
    if tagName == "img":
        src = child.get("src")
        if not src.startswith("http") and not src.startswith("https"):
            src = prefix_url + src
        markdownImageStr = mdFile.new_inline_image("", src)
        mdFile.new_line(markdownImageStr)
        # print(src)
    if tagName == "ol":
        liList = child.find_all("li")
        for li in liList:
            divInli = li.css.select("div")
            textStrings = divInli[0].strings
            # li中包含加粗的信息，因此要通过列表来拼接全部内容
            completeString = ""
            for textString in textStrings:
                completeString = completeString + textString
            mdFile.new_paragraph(completeString)
            translatedCompleteString = translate.translate(completeString)
            mdFile.new_paragraph(translatedCompleteString)
            print(completeString)

            if len(divInli) > 1:
                img = divInli[1].css.select_one("img")
                src = img.get("src")
                if not src.startswith("http") and not src.startswith("https"):
                    src = prefix_url + src
                markdownImageStr = mdFile.new_inline_image("", src)
                mdFile.new_line(markdownImageStr)
                print(src)
    if tagName == "pre":
        mdFile.insert_code(child.string, "java")
        print(child.string)
mdFile.create_md_file()
