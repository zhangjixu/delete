# -*- coding: utf-8 -*-

from api import app


@app.route("/")
def test_api():
    return "hello, world!"
