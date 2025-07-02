from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello from Railway Flask App by Asad Mirza!</h1>"

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
