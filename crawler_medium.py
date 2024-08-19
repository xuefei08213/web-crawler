import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import translate
from mdutils import MdUtils

prefix_url = "https://www.permit.io/"
URL = "https://blog.stackademic.com/frontend-masters-feature-sliced-design-fsd-pattern-81416088b006"

# url = f'https://medium.com/swlh/archive/2019/01/01'

dr = webdriver.Chrome()
dr.get(URL)


# bs = BeautifulSoup(dr.page_source,"html.parser")

# soup = BeautifulSoup(page.text, 'html.parser')


# article = soup.article
# section = article.find_one("section")
# print(bs.prettify())
# h1 = article.h1.string.strip()
# mdFile = MdUtils(file_name=h1, title=h1)
# mdFile.new_header(level=1, title=h1)
#
# imgInHeader = article.header.find("img")
# imgSrc = imgInHeader.get("src")
# markdownImageStr = mdFile.new_inline_image("", imgSrc)
# mdFile.new_line(markdownImageStr)
#
# # 文章的主体内容放在一个id为article-body的div中
# articleBodyDiv = article.find(id="article-body")
# # print(articleBodyDiv.prettify())
#
# children = articleBodyDiv.children
#
# for child in children:
#     tagName = child.name
#     # print(child.name)
#     if tagName == "h2" or tagName == "h3":
#         """
#         h2中的内容包括a标签和内容，如下
#         <h2>
#           <a name="beginnings" href="#beginnings">
#           </a>
#           Beginnings
#         </h2>
#         针对上面的情况，只获取第二个
#         """
#         contentsInHTag = child.children
#         completeString = ""
#         # p中包含加粗的信息，因此要通过列表来拼接全部内容
#         for content in contentsInHTag:
#             completeString = completeString + content.string.strip()
#             translatedHString = translate.translate(completeString)
#             print(translatedHString)
#         if (tagName == "h2"):
#             mdFile.new_header(level=2, title=completeString)
#             mdFile.new_header(level=2, title=translatedHString)
#         elif (tagName == "h3"):
#             mdFile.new_header(level=3, title=completeString)
#             mdFile.new_header(level=3, title=translatedHString)
#     if tagName == "p":
#         contentsInPTag = child.children
#         completeString = ""
#         # p中包含加粗的信息，因此要通过列表来拼接全部内容
#         for content in contentsInPTag:
#             completeString = completeString + content.string
#         mdFile.new_paragraph(completeString)
#         translatedCompleteString = translate.translate(completeString)
#         print(translatedCompleteString)
#         mdFile.new_paragraph(translatedCompleteString)
#         # print(completeString)
#     if tagName == "img":
#         src = child.get("src")
#         if not src.startswith("http") and not src.startswith("https"):
#             src = prefix_url + src
#         markdownImageStr = mdFile.new_inline_image("", src)
#         mdFile.new_line(markdownImageStr)
#     if tagName == "blockquote":
#         for string in child.stripped_strings:
#             stringEscape = string.replace("-", "`-`")
#             mdFile.new_line(">" + stringEscape)
#             translatedStringEscape = translate.translate(stringEscape)
#             print(translatedStringEscape)
#             mdFile.new_line(">" + translatedStringEscape)
            # print(repr(string))
        # print(src)
    # if tagName == "ol":
    #     liList = child.find_all("li")
    #     for li in liList:
    #         divInli = li.css.select("div")
    #         textStrings = divInli[0].strings
    #         # li中包含加粗的信息，因此要通过列表来拼接全部内容
    #         completeString = ""
    #         for textString in textStrings:
    #             completeString = completeString + textString
    #         mdFile.new_paragraph(completeString)
    #         # translatedCompleteString = translate.translate(completeString)
    #         # mdFile.new_paragraph(translatedCompleteString)
    #         print(completeString)
    #
    #         if len(divInli) > 1:
    #             img = divInli[1].css.select_one("img")
    #             src = img.get("src")
    #             if not src.startswith("http") and not src.startswith("https"):
    #                 src = prefix_url + src
    #             markdownImageStr = mdFile.new_inline_image("", src)
    #             mdFile.new_line(markdownImageStr)
    #             print(src)
    # if tagName == "pre":
    #     mdFile.insert_code(child.string, "java")
    #     print(child.string)
# mdFile.create_md_file()
