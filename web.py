from flask import Flask, redirect, abort, render_template

from models import Files

app = Flask(__name__, template_folder="template", static_folder="static")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/<target_name>")
def social_media_redirecter(target_name):
    social_urls = Files().get_social_urls()
    target_name = target_name.lower()
    if target_name in social_urls:
        return redirect(social_urls[target_name], code=302)
    abort(404)


if __name__ == "__main__":
    app.run(debug=True)
