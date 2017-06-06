# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1496709591.690974
_enable_loop = True
_template_filename = u'themes/canterville/templates/post.tmpl'
_template_uri = u'post.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content', u'extra_head']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'pheader', context._clean_inheritance_tokens(), templateuri=u'post_header.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'pheader')] = ns

    ns = runtime.TemplateNamespace(u'comments', context._clean_inheritance_tokens(), templateuri=u'comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'comments')] = ns

    ns = runtime.TemplateNamespace(u'helper', context._clean_inheritance_tokens(), templateuri=u'post_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'helper')] = ns

    ns = runtime.TemplateNamespace(u'math', context._clean_inheritance_tokens(), templateuri=u'math_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'math')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        parent = context.get('parent', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        date_format = context.get('date_format', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        author_pages_generated = context.get('author_pages_generated', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        comments = _mako_get_namespace(context, 'comments')
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        post = context.get('post', UNDEFINED)
        math = _mako_get_namespace(context, 'math')
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

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
        date_format = context.get('date_format', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        author_pages_generated = context.get('author_pages_generated', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        def content():
            return render_content(context)
        comments = _mako_get_namespace(context, 'comments')
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        post = context.get('post', UNDEFINED)
        math = _mako_get_namespace(context, 'math')
        __M_writer = context.writer()
        __M_writer(u'\n\n  <article class="post post">\n    <header class="post-header">\n        <h1 class="post-title">')
        __M_writer(unicode(post.title()))
        __M_writer(u'</h1>\n        <section class="post-meta"> by\n')
        if author_pages_generated:
            __M_writer(u'            <a href="')
            __M_writer(unicode(_link('author', post.author())))
            __M_writer(u'">')
            __M_writer(filters.html_escape(unicode(post.author())))
            __M_writer(u'</a>\n')
        else:
            __M_writer(u'            ')
            __M_writer(filters.html_escape(unicode(post.author())))
            __M_writer(u'\n')
        __M_writer(u'            on\n')
        for tag in post.tags:
            __M_writer(u'                <a href="link://tag/')
            __M_writer(unicode(tag))
            __M_writer(u'">#')
            __M_writer(unicode(tag))
            __M_writer(u'</a>,\n')
        __M_writer(u'            <time class="post-date" datetime="')
        __M_writer(unicode(post.formatted_date('webiso')))
        __M_writer(u'">\n                ')
        __M_writer(filters.html_escape(unicode(post.formatted_date(date_format))))
        __M_writer(u'\n            </time>\n        </section>\n    </header>\n\n    <section class="post-content">\n    ')
        __M_writer(unicode(post.text()))
        __M_writer(u'\n    </section>\n    <footer class="post-footer">\n')
        if not post.meta('nocomments') and site_has_comments:
            __M_writer(u'        <section class="comments hidden-print">\n        <h2>')
            __M_writer(unicode(messages("Comments")))
            __M_writer(u'</h2>\n        ')
            __M_writer(unicode(comments.comment_form(post.permalink(absolute=True), post.title(), post._base_path)))
            __M_writer(u'\n        </section>\n')
        __M_writer(u'    ')
        __M_writer(unicode(math.math_scripts_ifpost(post)))
        __M_writer(u'\n</article>\n')
        __M_writer(unicode(comments.comment_link_script()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def extra_head():
            return render_extra_head(context)
        post = context.get('post', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        parent = context.get('parent', UNDEFINED)
        math = _mako_get_namespace(context, 'math')
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(unicode(parent.extra_head()))
        __M_writer(u'\n')
        if post.meta('keywords'):
            __M_writer(u'    <meta name="keywords" content="')
            __M_writer(filters.html_escape(unicode(post.meta('keywords'))))
            __M_writer(u'">\n')
        __M_writer(u'    <meta name="author" content="')
        __M_writer(filters.html_escape(unicode(post.author())))
        __M_writer(u'">\n')
        if post.prev_post:
            __M_writer(u'        <link rel="prev" href="')
            __M_writer(unicode(post.prev_post.permalink()))
            __M_writer(u'" title="')
            __M_writer(filters.html_escape(unicode(post.prev_post.title())))
            __M_writer(u'" type="text/html">\n')
        if post.next_post:
            __M_writer(u'        <link rel="next" href="')
            __M_writer(unicode(post.next_post.permalink()))
            __M_writer(u'" title="')
            __M_writer(filters.html_escape(unicode(post.next_post.title())))
            __M_writer(u'" type="text/html">\n')
        if post.is_draft:
            __M_writer(u'        <meta name="robots" content="noindex">\n')
        __M_writer(u'    ')
        __M_writer(unicode(helper.open_graph_metadata(post)))
        __M_writer(u'\n    ')
        __M_writer(unicode(helper.twitter_card_information(post)))
        __M_writer(u'\n    ')
        __M_writer(unicode(helper.meta_translations(post)))
        __M_writer(u'\n    ')
        __M_writer(unicode(math.math_styles_ifpost(post)))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"23": 3, "26": 4, "29": 2, "32": 5, "38": 0, "57": 2, "58": 3, "59": 4, "60": 5, "61": 6, "66": 27, "71": 63, "77": 29, "91": 29, "92": 33, "93": 33, "94": 35, "95": 36, "96": 36, "97": 36, "98": 36, "99": 36, "100": 37, "101": 38, "102": 38, "103": 38, "104": 40, "105": 41, "106": 42, "107": 42, "108": 42, "109": 42, "110": 42, "111": 44, "112": 44, "113": 44, "114": 45, "115": 45, "116": 51, "117": 51, "118": 54, "119": 55, "120": 56, "121": 56, "122": 57, "123": 57, "124": 60, "125": 60, "126": 60, "127": 62, "128": 62, "134": 8, "144": 8, "145": 9, "146": 9, "147": 10, "148": 11, "149": 11, "150": 11, "151": 13, "152": 13, "153": 13, "154": 14, "155": 15, "156": 15, "157": 15, "158": 15, "159": 15, "160": 17, "161": 18, "162": 18, "163": 18, "164": 18, "165": 18, "166": 20, "167": 21, "168": 23, "169": 23, "170": 23, "171": 24, "172": 24, "173": 25, "174": 25, "175": 26, "176": 26, "182": 176}, "uri": "post.tmpl", "filename": "themes/canterville/templates/post.tmpl"}
__M_END_METADATA
"""
