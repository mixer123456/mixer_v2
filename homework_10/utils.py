from pywebio.session import run_js

def reload_page(time_ms: int) -> None:
    time_ms = str(time_ms)
    run_js('setTimeout(function(){location.reload();}, ' + time_ms + ')')
