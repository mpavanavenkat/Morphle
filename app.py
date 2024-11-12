from flask import Flask
import subprocess
import time
import os

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Pavana venkat"  # Replace with your actual name
    username = os.getlogin()
    server_time = time.strftime("%Y-%m-%d %H:%M:%S %Z", time.gmtime())
    top_output = subprocess.getoutput("top -b -n 1")

    return f"""
    <h1>Name: {name}</h1>
    <h2>User: {username}</h2>
    <h2>Server Time (IST): {server_time}</h2>
    <pre>TOP output:\n{top_output}</pre>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
