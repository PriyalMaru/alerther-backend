from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "AlertHer backend is running!"

@app.route("/alert")
def alert():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    emergency_type = request.args.get('type', 'Emergency')

    print("🚨 ALERT RECEIVED!")
    print("Type:", emergency_type)
    print("Location:", lat + ", " + lon)
    print("Google Maps: https://maps.google.com/?q=" + lat + "," + lon)

    return "Alert Triggered"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)