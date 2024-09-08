from flask import Flask, request

from crawler.crawler_dev_to import crawler_dev_to
from crawler.crawler_medium import crawler_medium

app = Flask(__name__)

@app.route('/crawler/dev_to',methods=['POST'])
def dev_to():
    data = request.get_json()
    url = data['url']
    crawler_dev_to(url)
    return "success"


@app.route('/crawler/medium',methods=['POST'])
def medium():
    data = request.get_json()
    url = data['url']
    crawler_medium(url)

    return "success"


if __name__ == '__main__':
    app.run()