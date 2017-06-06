# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1496709591.340309
_enable_loop = True
_template_filename = u'themes/canterville/templates/base.tmpl'
_template_uri = u'base.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content', u'extra_head', u'extra_js']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'header', context._clean_inheritance_tokens(), templateuri=u'base_header.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'header')] = ns

    ns = runtime.TemplateNamespace(u'base', context._clean_inheritance_tokens(), templateuri=u'base_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'base')] = ns

    ns = runtime.TemplateNamespace(u'annotations', context._clean_inheritance_tokens(), templateuri=u'annotation_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'annotations')] = ns

    ns = runtime.TemplateNamespace(u'footer', context._clean_inheritance_tokens(), templateuri=u'base_footer.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'footer')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, u'header')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'footer')._populate(_import_ns, [u'*'])
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        body_end = _import_ns.get('body_end', context.get('body_end', UNDEFINED))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        BANNER_URL = _import_ns.get('BANNER_URL', context.get('BANNER_URL', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        TWITTER_URL = _import_ns.get('TWITTER_URL', context.get('TWITTER_URL', UNDEFINED))
        footer = _mako_get_namespace(context, 'footer')
        set_locale = _import_ns.get('set_locale', context.get('set_locale', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        header = _mako_get_namespace(context, 'header')
        pagekind = _import_ns.get('pagekind', context.get('pagekind', UNDEFINED))
        base = _mako_get_namespace(context, 'base')
        def extra_js():
            return render_extra_js(context._locals(__M_locals))
        blog_url = _import_ns.get('blog_url', context.get('blog_url', UNDEFINED))
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        logo_url = _import_ns.get('logo_url', context.get('logo_url', UNDEFINED))
        GITHUB_URL = _import_ns.get('GITHUB_URL', context.get('GITHUB_URL', UNDEFINED))
        description = _import_ns.get('description', context.get('description', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(unicode(set_locale(lang)))
        __M_writer(u'\n')
        __M_writer(unicode(base.html_headstart()))
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer(u'\n')
        __M_writer(unicode(template_hooks['extra_head']()))
        __M_writer(u'\n</head>\n<body class="nav-closed">\n')
        __M_writer(unicode(header.html_navigation_links()))
        __M_writer(u'\n<div class="site-wrapper">\n')
        if 'main_index' in pagekind and BANNER_URL :
            __M_writer(u'    <header class="main-header" style="background-image: url(')
            __M_writer(unicode(BANNER_URL))
            __M_writer(u')">\n')
        elif 'post_page' in pagekind and post.meta('banner'):
            __M_writer(u'    <header class="main-header" style="background-image: url(')
            __M_writer(unicode(post.meta('banner')))
            __M_writer(u')">\n')
        else:
            __M_writer(u'    <header class="main-header post-head no-cover">\n')
        __M_writer(u'        <nav class="main-nav overlay clearfix">\n            <a class="blog-logo" href="')
        __M_writer(unicode(blog_url))
        __M_writer(u'"><img src="')
        __M_writer(unicode(logo_url))
        __M_writer(u'" alt="Blog Logo" /></a>\n            <a class="menu-button" href="#"><span class="burger">&#9776;</span><span class="word">Menu</span></a>\n        </nav>\n')
        if 'main_index' in pagekind:
            __M_writer(u'        <div class="vertical">\n            <div class="main-header-content inner">\n')
            if GITHUB_URL:
                __M_writer(u'                <a  href="')
                __M_writer(unicode(GITHUB_URL))
                __M_writer(u'" target="_blank">\n                    <span class="icon-github" style="color:white;font-size:2em"></span>\n                </a>\n                &nbsp;\n')
            if TWITTER_URL:
                __M_writer(u'                <a class="bloglogo" href=')
                __M_writer(unicode(TWITTER_URL))
                __M_writer(u' target="_blank">\n                    <span class="icon-twitter" style="color:white;font-size:2em"></span>\n                </a>\n                &nbsp;\n')
            __M_writer(u'                <h1 class="page-title">')
            __M_writer(unicode(title))
            __M_writer(u'</h1>\n                <h2 class="page-description">')
            __M_writer(unicode(description))
            __M_writer(u'</h2>\n            </div>\n        </div>\n        <a class="scroll-down icon-arrow-left" href="#content"><span class="hidden">Scroll Down</span></a>\n')
        __M_writer(u'    </header>\n\n    <main id="content" class="content" role="main">\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer(u'\n    </main>\n    ')
        __M_writer(unicode(footer.html_footer()))
        __M_writer(u'\n</div>\n')
        __M_writer(unicode(base.late_load_js()))
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_js'):
            context['self'].extra_js(**pageargs)
        

        __M_writer(u'\n')
        __M_writer(unicode(body_end))
        __M_writer(u'\n')
        __M_writer(unicode(template_hooks['body_end']()))
        __M_writer(u'\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'header')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'footer')._populate(_import_ns, [u'*'])
        def content():
            return render_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'header')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'footer')._populate(_import_ns, [u'*'])
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_js(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'header')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'footer')._populate(_import_ns, [u'*'])
        def extra_js():
            return render_extra_js(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"128": 57, "129": 57, "130": 58, "131": 58, "137": 51, "23": 3, "152": 8, "26": 2, "29": 5, "32": 4, "162": 8, "35": 0, "168": 56, "183": 168, "66": 2, "67": 3, "68": 4, "69": 5, "70": 6, "71": 6, "72": 7, "73": 7, "78": 10, "79": 11, "80": 11, "81": 14, "82": 14, "83": 16, "84": 17, "85": 17, "86": 17, "87": 18, "88": 19, "89": 19, "90": 19, "91": 20, "92": 21, "93": 23, "94": 24, "95": 24, "96": 24, "97": 24, "98": 27, "99": 28, "100": 30, "101": 31, "102": 31, "103": 31, "104": 36, "105": 37, "106": 37, "107": 37, "108": 42, "109": 42, "110": 42, "111": 43, "112": 43, "113": 48, "118": 51, "119": 53, "120": 53, "121": 55, "122": 55, "127": 56}, "uri": "base.tmpl", "filename": "themes/canterville/templates/base.tmpl"}
__M_END_METADATA
"""
