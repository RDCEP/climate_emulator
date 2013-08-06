from datetime import datetime
from flask import Flask
from flask import render_template, request, jsonify
from emulator.emulator import Emulator
from flask_beaker import BeakerSession


session_opts = {
    'session.type': 'ext:memcached',
    'session.cookie_expires': True,
    'session.lock_dir': './data',
    'session.url': '127.0.0.1:11211',
    'session.memcache_module': 'pylibmc',
    'session.auto': True
}

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'Ad78gii#$3979oklaklf'
BeakerSession(app)


def do_session(new=False):
    """
    Checks for existence of session data. Writes variables as necessary.
    ...
    Keyword Arguments:
    newdice: obj
        A Dice2007 object.
    """
    s = request.environ['beaker.session']
    if new:
        e = new
        s['emulator'] = e
        s.save()
    if 'emulator' not in s:
        e = Emulator()
        s['emulator'] = e
        s.save()
    return s


def page(tpl='index.html'):
    """
    Return HTML for all pages.
    ...
    Args:
        template
    Returns:
        HTML
    """
    now = datetime.now().strftime('%Y%m%d%H%M%S')
    print now
    t = render_template(
        tpl,
        now=now,
    )
    return t

@app.route('/')
def index():
    """Returns index page."""
    do_session()
    return page('index.html')

# @app.route('/model/<model>/rcp/<rcp>/temp/<temp>', methods=['POST', ])
@app.route('/model/<model>/rcp/<rcp>/temp/<temp>', methods=['POST', 'GET', ])
def rcp(model, rcp, temp):
    if request.method == 'GET':
        e = do_session()['emulator']
        return jsonify(e.get_model_rcp_output(
            model=model, rcp=rcp, temp=temp
        ))


@app.route('/csv_upload', methods=['POST', 'GET', ])
def csv_upload():
    if request.method == 'POST':
        csv = request.files['csv']
        new_rcp = [float(n) for n in csv.read().split(',')]
        if len(new_rcp) != 96:
            return 'Your CSV file needs to have 1 row of 96 values.', 501
        e = do_session()['emulator']
        return jsonify(e.get_model_rcp_output(co2=new_rcp))


if __name__ == '__main__':
    app.run()
