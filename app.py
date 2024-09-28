from flask import Flask, render_template
from scraper import get_all_news

app = Flask(__name__)

@app.route('/')
def home():
    news = get_all_news()
    # Ordina le notizie in base al timestamp
    sorted_news = sorted(news, key=lambda x: x['timestamp'], reverse=True)
    return render_template('index.html', news=sorted_news)

if __name__ == '__main__':
    app.run(debug=True)
