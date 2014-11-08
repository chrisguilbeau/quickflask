from web import html
from web import t

def index():
    return t.html(
        t.head(),
        t.body(
            t.span('this is quickflask'),
            ),
        )

def flex():
    return t.html(
        t.head(
            t.link(rel='stylesheet', href='/s/flex.css'),
            ),
        t.body(
            t.div(
                t.div('top', _class='top tight'),
                t.div('middle', _class='middle'),
                t.div('bottom', _class='bottom tight'),
                _class='main flex-col flex-expand',
                ),
            ),
        )
