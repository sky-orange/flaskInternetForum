from flask import Flask, render_template, redirect, request, url_for
import json
app = Flask(__name__)


def load_threads_data():
    global threads_data
    with open("threadsData.json") as json_data:
        threads_data = json.load(json_data)


def save_threads_data():
    with open("threadsData.json", "w") as outfile:
        json.dump(threads_data, outfile, indent=2)


try:
    load_threads_data()
except IOError:
    threads_data = {}


@app.route("/thread/<thread_number>/create-new-comment", methods=["POST"])
def add_new_comment(thread_number):
    global threads_data
    threads_data[thread_number]["comments"].append(request.form.to_dict())
    save_threads_data()
    return redirect("thread/" + thread_number)


@app.route("/create-new-thread", methods=["POST"])
def create_new_thread():
    global threads_data
    new_thread_number = str(len(threads_data))
    threads_data[new_thread_number] = request.form.to_dict()
    threads_data[new_thread_number]["comments"] = []
    save_threads_data()
    return redirect(url_for("thread_page", thread_number=new_thread_number))


@app.route("/")
def main_page():
    return render_template("mainPage.html", threads=threads_data)


@app.route("/thread/<thread_number>/", methods=["GET"])
def thread_page(thread_number):
    return render_template("threadPage.html", thread=threads_data[thread_number])
