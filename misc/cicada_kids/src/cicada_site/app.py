from flask import Flask, render_template, request
import requests, os, json

app = Flask(__name__)

API_KEY = os.environ.get(
    "CTFD_API_KEY",
    "ctfd_2c71a65dc478092a47cdebf982b250337ba33b3f15505001fd0dbec10f62b89e",
)
API_URL = f"""{os.environ.get("CTFD_URL", "https://krductf.ru")}/api/v1/challenges/{os.environ.get("CTFD_TASK_ID", 87)}/solves"""

headers = {
    "Authorization": f"Token {API_KEY}",
    "Content-Type": "application/json",
}


responses = {
    "привет": "Привет! Как дела?",
    "как дела?": "Хорошо, спасибо. А у тебя?",
    "пока": "До свидания! Возвращайся скоро.",
}


@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.form["user_input"].lower()
    response = responses.get(user_input, "Извините, не могу понять ваш запрос.")
    return render_template("storage.html", user_input=user_input, response=response)


@app.route("/")
def index():
    r = requests.get(API_URL, headers=headers)

    if r.status_code == 200:
        data = r.json()["data"]
        return render_template("index.html", users=data)
    else:
        return render_template("index.html")


@app.route("/327a6c4304ad5938eaf0efb6cc3e53dc")
def flag():
    return render_template("flag.html")


@app.route("/c98a679441798bdb9c194f9ca471e6cd")
def level_1():
    return render_template("math.html")


@app.route("/4eb5d6bd65ed1b4f5ac431b04a2cac1f")
def level_2():
    return render_template("storage.html")


@app.route("/ee54449478c54a5a5cc4f774e3d4ba34")
def level_3():
    return render_template("level_3.html")


@app.route("/49e3c1983311a275fadc1509148f7ff1")
def level_4():
    return render_template("level_4.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
