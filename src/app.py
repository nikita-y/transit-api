#!flask/bin/python
from flask import Flask, jsonify, make_response, request
from gtfs_mixin import *

app = Flask(__name__)
gtfs = GTFS()


@app.route('/transit/api/v1/next', methods=['GET'])
def get_next_schedules():
    origin = request.args.get("origin_station_id")
    destination = request.args.get("destination_station_id")
    lat = request.args.get("latitude")
    lng = request.args.get("longitude")

    if (origin == "" or destination == ""):
        return make_response(jsonify({'error': 'Bad request'}), 400)

    schedules = gtfs.schedules(origin, destination)
    return jsonify({'next_schedules': schedules})


@ app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
