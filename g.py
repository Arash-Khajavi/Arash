from flask import Flask, request, abort
import requests
import os
app = Flask(__name__)
o=os.getenv("IP")
API_KEY = o
BLOCKED_COUNTRY = "Iran"  # Replace with the country you want to block

def get_country(ip):
    """Get country from IP using IPstack API."""
    url = f"http://api.ipstack.com/{ip}?access_key={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data.get("country_name", "Unknown")  # Get country or return "Unknown"

@app.before_request
def block_countries():
    """Block users from a specific country."""
    ip = request.remote_addr  # Get client IP address
    country = get_country(ip)

    if country == BLOCKED_COUNTRY:
        abort(403)  # Forbidden access

@app.route("/")
def home():
    return "Welcome to my Flask app!"

if __name__ == "__main__":
    app.run(debug=True)
