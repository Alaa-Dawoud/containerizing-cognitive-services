from flask import Flask, request, render_template, Response
from computer_vision import get_analytics
app = Flask(__name__)


@app.route('/')
def index():
    return "hello world test test test"


@app.route('/sample-video')
def video():
    return render_template('index.html')


@app.route('/computer-vision', methods=['POST'])
def computer_vision():
    search_img = request.args.get("image")
    output_analysis = get_analytics(search_img)
    return output_analysis


if __name__ == '__main__':
    app.run(port=5000)
