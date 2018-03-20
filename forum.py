from flask import Flask, render_template, redirect, request
import json
app = Flask(__name__)


try:
    with open("threadData.json") as json_data:
        thread_data = json.load(json_data)
except IOError:
    thread_data = {}


def save_thread_data():
    with open("threadData.json", "w") as outfile:
        json.dump(thread_data, outfile)


@app.route("/")
def main_page():
    return render_template("mainPage.html", threads=thread_data)


@app.route("/create-new-thread", methods=["POST", "GET"])
def create_new_thread():
    new_thread_number = len(thread_data)
    thread_data[new_thread_number] = request.form
    save_thread_data()
    new_thread_url = "/thread/" + str(new_thread_number)
    return redirect(new_thread_url)


@app.route("/thread/<url>")
def thread_page(url):
    return render_template("threadPage.html")
