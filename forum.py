from flask import Flask, render_template, redirect, request, url_for
import json
app = Flask(__name__)


try:
    with open("threadsData.json") as json_data:
        threads_data = json.load(json_data)
except IOError:
    threads_data = {}


def save_thread_data():
    with open("threadsData.json", "w") as outfile:
        json.dump(threads_data, outfile)


def add_new_comment():
    pass


@app.route("/")
def main_page():
    return render_template("mainPage.html", threads=threads_data)


@app.route("/create-new-thread", methods=["POST", "GET"])
def create_new_thread():
    global threads_data
    new_thread_number = str(len(threads_data))
    threads_data[new_thread_number] = request.form
    save_thread_data()
    return redirect(url_for("thread_page", thread_number=new_thread_number))


@app.route("/thread/<thread_number>", methods=["POST", "GET"])
def thread_page(thread_number):
    if request.method=="POST" and "New comment" in request.form:
        add_new_comment()
    return render_template("threadPage.html", thread=threads_data[thread_number])
