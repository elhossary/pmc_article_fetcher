from flask import Flask
from pmc_article_fetcher import PMCArticleFetcher

app = Flask(__name__)


@app.route('/<string:pmcid>', methods=['GET'])
def hello_world(pmcid):
    return PMCArticleFetcher(pmcid).fetch_article()


if __name__ == '__main__':
    app.run()
