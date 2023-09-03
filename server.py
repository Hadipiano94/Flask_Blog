from flask import Flask, render_template
import datetime as dt
import requests
from post import Post

app = Flask(__name__)
current_year = dt.datetime.now().year


posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

post_objects = []

for post in posts:
    post_objects.append(Post(post["id"], post["body"], post["title"], post["subtitle"]))


@app.route("/")
def get_home():
    return render_template("index.html", year=current_year)


@app.route("/blog")
def get_blog():
    return render_template("blog.html", year=current_year, all_posts=post_objects)


@app.route("/blog/post/<my_id>")
def get_post(my_id):
    the_post = [my_post for my_post in post_objects if my_post.id == int(my_id)][0]
    return render_template("post.html", the_post=the_post, year=current_year)


if __name__ == "__main__":
    app.run(debug=True)
