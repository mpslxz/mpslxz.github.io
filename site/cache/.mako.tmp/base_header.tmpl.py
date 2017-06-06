# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1496709591.485404
_enable_loop = True
_template_filename = u'themes/canterville/templates/base_header.tmpl'
_template_uri = u'base_header.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_navigation_links', 'html_translation_header', 'html_header', 'html_site_title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'base', context._clean_inheritance_tokens(), templateuri=u'base_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'base')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_navigation_links(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        navigation_links = _import_ns.get('navigation_links', context.get('navigation_links', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        rel_link = _import_ns.get('rel_link', context.get('rel_link', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n<div class="nav">\n    <h3 class="nav-title">Menu</h3>\n    <a href="#" class="nav-close">\n        <span class="hidden">Close</span>\n    </a>\n    <ul>\n')
        for url, text in navigation_links[lang]:
            if rel_link(permalink, url) == "#":
                __M_writer(u'        <li class="nav-opened nav-current" role="presentation">\n')
            else:
                __M_writer(u'        <li class="nav-opened" role="presentation">\n')
            __M_writer(u'            <a href="')
            __M_writer(unicode(url))
            __M_writer(u'">')
            __M_writer(unicode(text))
            __M_writer(u'</a>\n        </li>\n')
        __M_writer(u'    ')
        __M_writer(unicode(template_hooks['menu']()))
        __M_writer(u'\n    ')
        __M_writer(unicode(template_hooks['menu_alt']()))
        __M_writer(u'\n    </ul>\n</div>\n<span class="nav-cover"></span>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translation_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        base = _mako_get_namespace(context, 'base')
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        if len(translations) > 1:
            __M_writer(u'        <div id="toptranslations">\n            <h2>')
            __M_writer(unicode(messages("Languages:")))
            __M_writer(u'</h2>\n            ')
            __M_writer(unicode(base.html_translations()))
            __M_writer(u'\n        </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        search_form = _import_ns.get('search_form', context.get('search_form', UNDEFINED))
        def html_navigation_links():
            return render_html_navigation_links(context)
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        def html_translation_header():
            return render_html_translation_header(context)
        def html_site_title():
            return render_html_site_title(context)
        __M_writer = context.writer()
        __M_writer(u'\n    <header id="header">\n        ')
        __M_writer(unicode(html_site_title()))
        __M_writer(u'\n        ')
        __M_writer(unicode(html_translation_header()))
        __M_writer(u'\n        ')
        __M_writer(unicode(html_navigation_links()))
        __M_writer(u'\n')
        if search_form:
            __M_writer(u'            <div class="searchform" role="search">\n                ')
            __M_writer(unicode(search_form))
            __M_writer(u'\n            </div>\n')
        __M_writer(u'    </header>\n    ')
        __M_writer(unicode(template_hooks['page_header']()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_site_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        show_blog_title = _import_ns.get('show_blog_title', context.get('show_blog_title', UNDEFINED))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        abs_link = _import_ns.get('abs_link', context.get('abs_link', UNDEFINED))
        logo_url = _import_ns.get('logo_url', context.get('logo_url', UNDEFINED))
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n    <h1 id="brand"><a href="')
        __M_writer(unicode(abs_link(_link("root", None, lang))))
        __M_writer(u'" title="')
        __M_writer(filters.html_escape(unicode(blog_title)))
        __M_writer(u'" rel="home">\n')
        if logo_url:
            __M_writer(u'        <img src="')
            __M_writer(unicode(logo_url))
            __M_writer(u'" alt="')
            __M_writer(filters.html_escape(unicode(blog_title)))
            __M_writer(u'" id="logo">\n')
        __M_writer(u'\n')
        if show_blog_title:
            __M_writer(u'        <span id="blog-title">')
            __M_writer(filters.html_escape(unicode(blog_title)))
            __M_writer(u'</span>\n')
        __M_writer(u'    </a></h1>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"130": 18, "151": 21, "142": 18, "143": 19, "144": 19, "145": 19, "146": 19, "147": 20, "148": 21, "149": 21, "150": 21, "23": 2, "152": 21, "153": 23, "26": 0, "155": 25, "156": 25, "154": 24, "158": 27, "33": 2, "34": 16, "35": 28, "36": 51, "37": 60, "43": 30, "157": 25, "54": 30, "55": 37, "56": 38, "57": 39, "58": 40, "59": 41, "60": 43, "61": 43, "62": 43, "63": 43, "64": 43, "65": 46, "66": 46, "67": 46, "68": 47, "69": 47, "75": 53, "164": 158, "85": 53, "86": 54, "87": 55, "88": 56, "89": 56, "90": 57, "91": 57, "97": 4, "111": 4, "112": 6, "113": 6, "114": 7, "115": 7, "116": 8, "117": 8, "118": 9, "119": 10, "120": 11, "121": 11, "122": 14, "123": 15, "124": 15}, "uri": "base_header.tmpl", "filename": "themes/canterville/templates/base_header.tmpl"}
__M_END_METADATA
"""
