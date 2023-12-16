#!/usr/bin/python3
""" Index view
"""
from flask import jsonify

from api.v1.views import app_views


@app_views.route('/api/v1/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of the web server
    """
    return jsonify({"status": "OK"})

if __name__ == "__main__":
    # python -m api.v1.app
    app.run(host="0.0.0.0", port=5000)
