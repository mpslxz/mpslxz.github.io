# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1497085421.031106
_enable_loop = True
_template_filename = u'/Users/mehran/anaconda2/lib/python2.7/site-packages/nikola/data/themes/base/templates/list.tmpl'
_template_uri = 'list.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'archive_nav', context._clean_inheritance_tokens(), templateuri=u'archive_navigation_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'archive_nav')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, u'archive_nav')._populate(_import_ns, [u'*'])
        def content():
            return render_content(context._locals(__M_locals))
        items = _import_ns.get('items', context.get('items', UNDEFINED))
        archive_nav = _mako_get_namespace(context, 'archive_nav')
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'archive_nav')._populate(_import_ns, [u'*'])
        def content():
            return render_content(context)
        items = _import_ns.get('items', context.get('items', UNDEFINED))
        archive_nav = _mako_get_namespace(context, 'archive_nav')
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n<article class="listpage">\n    <header>\n        <h1>')
        __M_writer(filters.html_escape(unicode(title)))
        __M_writer(u'</h1>\n    </header>\n    ')
        __M_writer(unicode(archive_nav.archive_navigation()))
        __M_writer(u'\n')
        if items:
            __M_writer(u'    <ul class="postlist">\n')
            for text, link, count in items:
                __M_writer(u'        <li><a href="')
                __M_writer(unicode(link))
                __M_writer(u'">')
                __M_writer(filters.html_escape(unicode(text)))
                __M_writer(u'</a>\n')
                if count:
                    __M_writer(u'            (')
                    __M_writer(unicode(count))
                    __M_writer(u')\n')
            __M_writer(u'    </ul>\n')
        else:
            __M_writer(u'    <p>')
            __M_writer(unicode(messages("Nothing found.")))
            __M_writer(u'</p>\n')
        __M_writer(u'</article>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"23": 3, "29": 0, "42": 2, "43": 3, "48": 24, "54": 5, "66": 5, "67": 8, "68": 8, "69": 10, "70": 10, "71": 11, "72": 12, "73": 13, "74": 14, "75": 14, "76": 14, "77": 14, "78": 14, "79": 15, "80": 16, "81": 16, "82": 16, "83": 19, "84": 20, "85": 21, "86": 21, "87": 21, "88": 23, "94": 88}, "uri": "list.tmpl", "filename": "/Users/mehran/anaconda2/lib/python2.7/site-packages/nikola/data/themes/base/templates/list.tmpl"}
__M_END_METADATA
"""
