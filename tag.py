from functools import partial
from collections import Iterable

def flatten(_list):
    for item in _list:
        if isinstance(item, Iterable) and not isinstance(item, basestring):
            for subItem in flatten(item):
                yield subItem
        else:
            yield item

def _tagAttrs(**kwargs):
    return " " + " ".join(
        '{}="{}"'.format(k.strip('_'), v)
        for k, v in kwargs.iteritems()
        )

def _tagContent(*args):
    return "".join(flatten(args))

def _tag(name, *args, **kwargs):
    return "<{name}{attrs}>{content}</{name}>".format(
        name=name,
        attrs=_tagAttrs(**kwargs) if kwargs else "",
        content=_tagContent(*args),
        )

class TagMeta(object.__class__):
    def __getattribute__(self, attr):
        return _tagContent if attr == '_' else partial(_tag, attr)

class Tag(object):
    __metaclass__ = TagMeta
