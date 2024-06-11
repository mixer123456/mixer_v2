from pywebio import start_server as start_server_pw
from pywebio.session import run_js


def start_server(main, port, filename):
    if filename == '__main__':
        start_server_pw(main, port=port)


def reload_page(time_ms: int) -> None:
    time_ms = str(time_ms)
    run_js('setTimeout(function(){location.reload();}, ' + time_ms + ')')
