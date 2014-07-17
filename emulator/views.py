from datetime import datetime
from flask import render_template, request, Blueprint, jsonify
from emulator import Emulator


mod = Blueprint('emulator', __name__, static_folder='static',
                template_folder='templates')


def do_session(new=False):
    """
    Checks for existence of session data. Writes variables as necessary.
    ...
    Keyword Arguments:
    new: obj
        An Emulator object.
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
    t = render_template(
        tpl,
        now=now,
    )
    return t


@mod.route('/')
def index():
    """Returns index page."""
    do_session()
    return page('index.html')


@mod.route('/rcp/<rcp>/temp/<temp>', methods=['GET', ])
def global_temp_by_model(rcp, temp):
    e = do_session()['emulator']
    return render_template(
        'index.html',
        rcp=rcp,
        temp=temp,
        region_type='global',
    )


@mod.route('/model/<model>/rcp/<rcp>/temp/<temp>', methods=['GET', ])
def regional_temp(model, rcp, temp):
    return render_template(
        'index.html',
        model=model,
        rcp=rcp,
        temp=temp,
    )


@mod.route('/api/model/<model>/rcp/<rcp>/temp/<temp>', methods=['POST', 'GET', ])
def rcp(model, rcp, temp):
    if request.method == 'GET':
        e = do_session()['emulator']
        return jsonify(e.get_model_rcp_output(
            model=model, rcp=rcp, temp=temp
        ))


@mod.route('/api/rcp/<rcp>/temp/<temp>')
def global_mean(rcp, temp):
    if request.method == 'GET':
        e = do_session()['emulator']
        return jsonify(e.get_mean_rcp_output(
            rcp=rcp, temp=temp
        ))


@mod.route('/csv_upload', methods=['POST', 'GET', ])
def csv_upload():
    if request.method == 'POST':
        csv = request.files['csv']
        new_rcp = [float(n) for n in csv.read().split(',')]
        print(new_rcp, len(new_rcp))
        if len(new_rcp) != 96:
            return 'Your CSV file needs to have 1 row of 96 values.', 501
        e = do_session()['emulator']
        return jsonify(e.get_model_rcp_output(co2=new_rcp))