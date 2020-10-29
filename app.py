from flask import Flask, request, render_template, redirect
from boltons import iterutils
import csv
import os
app = Flask(__name__)
members = []


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/registered", methods=["POST"])
def register():
    name = request.form.get("Name")
    print(name)
    with open("registered.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow([name])

    return render_template("thankyou.html", name=name)


@app.route("/shuffle")
def shuffle():
    with open("registered.csv", "r") as file:
        reader = csv.reader(file)
        members = list(reader)

    for xs in iterutils.chunked(members, 10):
        print(''.join(map(str, xs)))


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 6000))
    app.run(host='0.0.0.0', port=port, debug="True")
