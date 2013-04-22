from datetime import datetime
import bottle
from bottle import route, request, default_app, template, response
from beaker.middleware import SessionMiddleware
from emulator import Emulator

bottle.TEMPLATE_PATH = ['../templates/',]

session_opts = {
    'session.type': 'ext:memcached',
    'session.cookie_expires': True,
    'session.lock_dir': './data',
    'session.url': '127.0.0.1:11211',
    'session.memcache_module': 'pylibmc',
    'session.auto': True
}

def do_session(new=False):
    """
    Checks for existence of session data. Writes variables as necessary.
    ...
    Keyword Arguments:
    newdice: obj
        A Dice2007 object.
    """
    s = request.environ.get('beaker.session')
    if new:
        e = new
        s['emulator'] = e
    if 'emulator' not in s:
        e = Emulator()
        s['emulator'] = e
    return s

def page(tem='index'):
    """
    Return HTML for all pages.
    ...
    Args:
        template
    Returns:
        HTML
    """
    now = datetime.now().strftime('%Y%m%d%H%M%S')
    tpl = template(tem,
        now=now,
    )
    return tpl

@route('/')
def index():
    """Returns index page."""
    do_session()
    return page('index')

@route('/tmp')
def tmp():
    do_session()
    return page('tmp')


app = SessionMiddleware(default_app(), session_opts)
application = app