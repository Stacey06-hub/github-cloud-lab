from flask import Flask
import redis

app = Flask(__name__)

cache = redis.Redis(host="redis", port=6379, decode_responses=True)

@app.route("/")
def home():
    try:
        visits = cache.incr("visits")
    except Exception as e:
        return f"Redis error: {e}"
    return f"Visits: {visits}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
