#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
from flask_beaker import BeakerSession
from flask.ext.assets import Environment, Bundle
# from flask_restful import Api, reqparse


session_opts = {
    'session.type': 'ext:memcached',
    'session.cookie_expires': True,
    'session.lock_dir': './data',
    'session.url': '127.0.0.1:11211',
    'session.memcache_module': 'pylibmc',
    'session.auto': True
}


app = Flask(__name__)
app.config.from_object('config')
BeakerSession(app)


@app.errorhandler(404)
def not_found(error):
    return render_template('errors/404.html'), 404


@app.errorhandler(403)
def not_found(error):
    return render_template('errors/403.html'), 403


@app.errorhandler(500)
def not_found(error):
    return render_template('errors/500.html'), 500


# @app.context_processor
# def context_globals():
#     pass


# api = Api(app)
# api_parser = reqparse.RequestParser()


from emulator_web.views import mod as emulator_module
app.register_blueprint(emulator_module)

assets = Environment(app)
js = Bundle('js/app/input.js',
            'js/app/geopolitical/regions.js',
            'js/app/geopolitical/models.js',
            'js/app/emulator_output.js',
            'js/app/emulator_input.js',
            'js/app/emulator_map.js',
            'js/app/emulator_dropzone.js',
            'js/app/emulator_help.js',
            filters='jsmin', output='gen/emulator.js')
assets.register('js_emulator', js)
css = Bundle('css/main.css', filters='cssmin', output='gen/main.css')
assets.register('css_main', css)


if __name__ == '__main__':
    app.run()