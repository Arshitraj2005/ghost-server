from flask import Flask
app = Flask(name)

@app.route('/')
def home():
    return "Bot is alive"

if__name__== '__main__':
    app.run(host='0.0.0.0', port=10000)
