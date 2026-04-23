from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "AlertHer backend is running!"

@app.route("/alert")
def alert():
    lat = request.args.get("lat")
    lon = request.args.get("lon")
    emergency_type = request.args.get("type", "Emergency")

    print("🚨 ALERT RECEIVED!")
    print("Type:", emergency_type)
    print("Location:", lat, ",", lon)
    print("Google Maps: https://maps.google.com/?q=" + str(lat) + "," + str(lon))

    return jsonify({
        "status": "success",
        "message": "Alert triggered",
        "type": emergency_type,
        "lat": lat,
        "lon": lon
    })

if __name__ == "__main__":
    app.run(debug=True)