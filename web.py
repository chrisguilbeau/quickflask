from tag import Tag as t

def doctype():
    return '<!doctype html>'

def html(*args, **kwargs):
    return t._(
        doctype(),
        t.html(*args, **kwargs),
        )
