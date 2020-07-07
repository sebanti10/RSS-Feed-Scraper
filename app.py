from flask import Flask, render_template
import rss_feed
app = Flask(__name__)

feed_dict = rss_feed.feed_data()

@app.route("/")
def hello():
	return render_template('home.html', feed_dict=feed_dict)