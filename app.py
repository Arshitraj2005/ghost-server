from flask import Flask
import subprocess
import threading

app = Flask(name)

def run_stream():
    subprocess.call(["python", "stream.py"])

threading.Thread(target=run_stream).start()

@app.route('/')
def home():
    return "Bot is alive and streaming!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
