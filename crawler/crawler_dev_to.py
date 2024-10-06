import requests
import bs4.element
from bs4 import BeautifulSoup
from util import aitools
from mdutils import MdUtils
import shutil


def crawler_dev_to(url):
    prefix_url = "https://www.permit.io/"
    # URL = "https://dev.to/shantanu_jana/100-javascript-projects-with-source-code-59lo?ref=dailydev"
    # URL = "https://dev.to/buildwebcrumbs/creating-a-personal-brand-how-to-sell-yourself-as-a-developer-52po?ref=dailydev"

    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    article = soup.article
    h1 = article.h1.string.strip()
    translatedh1 = aitools.translate(h1)
    mdFile = MdUtils(file_name=h1, title=h1)
    mdFile.new_header(level=1, title=h1)
    mdFile.new_header(level=1, title=translatedh1)

    mdFile.new_line(url)

    imgInHeader = article.header.find("img")
    imgSrc = imgInHeader.get("src")
    markdownImageStr = mdFile.new_inline_image("", imgSrc)
    mdFile.new_line(markdownImageStr)

    # 文章的主体内容放在一个id为article-body的div中
    articleBodyDiv = article.find(id="article-body")
    # print(articleBodyDiv.prettify())

    children = articleBodyDiv.children

    for child in children:
        tagName = child.name
        # print(child.name)
        if tagName == "h2" or tagName == "h3":
            """
            h2中的内容包括a标签和内容，如下
            <h2>
              <a name="beginnings" href="#beginnings">
              </a>
              Beginnings
            </h2>
            针对上面的情况，只获取第二个
            """
            contentsInHTag = child.children
            completeString = ""
            # p中包含加粗的信息，因此要通过列表来拼接全部内容
            for content in contentsInHTag:
                completeString = completeString + content.string.strip()
                translatedHString = aitools.translate(completeString)
                print(translatedHString)
            if (tagName == "h2"):
                mdFile.new_line("## {}".format(completeString))
                mdFile.new_line("## {}".format(translatedHString))
            elif (tagName == "h3"):
                mdFile.new_line("### {}".format(completeString))
                mdFile.new_line("### {}".format(translatedHString))
        if tagName == "p":
            contentsInPTag = child.children
            completeString = ""
            # p中包含加粗的信息，因此要通过列表来拼接全部内容
            for content in contentsInPTag:
                # print(type(content))
                if isinstance(content, bs4.element.Tag):
                    print(content.name)
                    if isinstance(content.next, bs4.element.NavigableString):
                        completeString = completeString + content.next.string
                    elif isinstance(content.next, bs4.element.Tag) and content.next.name == "img":
                        src = content.next.attrs.get("src")
                        if not src.startswith("http") and not src.startswith("https"):
                            src = prefix_url + src
                        markdownImageStr = mdFile.new_inline_image("", src)
                        mdFile.new_line(markdownImageStr)
                    # if content.name == "a":
                    #     completeString = completeString + content.string
                else:
                    completeString = completeString + content.string
            mdFile.new_paragraph(completeString)
            translatedCompleteString = aitools.translate(completeString)
            # translatedCompleteString = completeString
            print(translatedCompleteString)
            mdFile.new_paragraph(translatedCompleteString)
            # print(completeString)
        if tagName == "img":
            src = child.get("src")
            if not src.startswith("http") and not src.startswith("https"):
                src = prefix_url + src
            markdownImageStr = mdFile.new_inline_image("", src)
            mdFile.new_line(markdownImageStr)
        if tagName == "blockquote":
            for string in child.stripped_strings:
                stringEscape = string.replace("-", "`-`")
                mdFile.new_line(">" + stringEscape)
                translatedStringEscape = aitools.translate(stringEscape)
                print(translatedStringEscape)
                mdFile.new_line(">" + translatedStringEscape)
        if tagName == "div":
            classname = ' '.join(child.get("class", [])).strip()
            if classname == "highlight js-code-highlight":
                pre_inner_html = child.prettify()
                code_info = aitools.extract_code_from_pre(pre_inner_html)
                mdFile.new_paragraph(code_info)
        if tagName == "ul":
            lis = child.find_all("li")
            li_text_arr = []
            for li in lis:
                li_text = li.text.strip()
                translated_li_text = aitools.translate(li_text)
                li_text_arr.append(li_text)
                li_text_arr.append(translated_li_text)
            mdFile.new_line()
            mdFile.new_list(li_text_arr)

    mdFile.create_md_file()

    shutil.move(h1 + ".md", "posts")
