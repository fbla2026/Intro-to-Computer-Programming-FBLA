from flask import Flask, render_template_string, request

app = Flask(__name__)

# Game State
pet = {
    "name": "Buddy",
    "fullness": 50,
    "money": 50,
    "health": 100
}

HTML_TEMPLATE = '''
<h1>Status for {{ name }}</h1>
<p>Money: ${{ money }} | Fullness: {{ fullness }}/100 | Health: {{ health }}</p>
<form action="/feed" method="post"><button>Feed Pet</button></form>
'''

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, **pet)

@app.route('/feed', methods=['POST'])
def feed():
    pet['fullness'] += 10
    pet['money'] -= 5
    return render_template_string(HTML_TEMPLATE, **pet)

if __name__ == '__main__':
    app.run(port=9000)