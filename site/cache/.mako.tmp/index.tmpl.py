# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1496709591.246974
_enable_loop = True
_template_filename = u'themes/canterville/templates/index.tmpl'
_template_uri = u'index.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content', u'extra_head', u'content_header']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'pagination', context._clean_inheritance_tokens(), templateuri=u'pagination_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'pagination')] = ns

    ns = runtime.TemplateNamespace(u'math', context._clean_inheritance_tokens(), templateuri=u'math_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'math')] = ns

    ns = runtime.TemplateNamespace(u'helper', context._clean_inheritance_tokens(), templateuri=u'index_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'helper')] = ns

    ns = runtime.TemplateNamespace(u'comments', context._clean_inheritance_tokens(), templateuri=u'comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'comments')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        prevlink = context.get('prevlink', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        comments = _mako_get_namespace(context, 'comments')
        front_index_header = context.get('front_index_header', UNDEFINED)
        index_file = context.get('index_file', UNDEFINED)
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        def content_header():
            return render_content_header(context._locals(__M_locals))
        _link = context.get('_link', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        math = _mako_get_namespace(context, 'math')
        parent = context.get('parent', UNDEFINED)
        author_pages_generated = context.get('author_pages_generated', UNDEFINED)
        pagination = _mako_get_namespace(context, 'pagination')
        nextlink = context.get('nextlink', UNDEFINED)
        pagekind = context.get('pagekind', UNDEFINED)
        page_links = context.get('page_links', UNDEFINED)
        index_teasers = context.get('index_teasers', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        current_page = context.get('current_page', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        prev_next_links_reversed = context.get('prev_next_links_reversed', UNDEFINED)
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
        pagination = _mako_get_namespace(context, 'pagination')
        prevlink = context.get('prevlink', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        author_pages_generated = context.get('author_pages_generated', UNDEFINED)
        def content_header():
            return render_content_header(context)
        posts = context.get('posts', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        nextlink = context.get('nextlink', UNDEFINED)
        def content():
            return render_content(context)
        math = _mako_get_namespace(context, 'math')
        pagekind = context.get('pagekind', UNDEFINED)
        prev_next_links_reversed = context.get('prev_next_links_reversed', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        current_page = context.get('current_page', UNDEFINED)
        index_teasers = context.get('index_teasers', UNDEFINED)
        front_index_header = context.get('front_index_header', UNDEFINED)
        page_links = context.get('page_links', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_header'):
            context['self'].content_header(**pageargs)
        

        __M_writer(u'\n')
        if 'main_index' in pagekind:
            __M_writer(u'    ')
            __M_writer(unicode(front_index_header))
            __M_writer(u'\n')
        if page_links:
            __M_writer(u'    ')
            __M_writer(unicode(pagination.page_navigation(current_page, page_links, prevlink, nextlink, prev_next_links_reversed)))
            __M_writer(u'\n')
        __M_writer(u'<div class="postindex">\n')
        for post in posts:
            __M_writer(u'\n\n<article class="post post">\n    <header class="post-header">\n        <h2 class="post-title"><a href="')
            __M_writer(unicode(post.permalink()))
            __M_writer(u'">')
            __M_writer(filters.html_escape(unicode(post.title())))
            __M_writer(u'</a></h2>\n    </header>\n')
            if index_teasers:
                __M_writer(u'    <section class="post-excerpt">\n    ')
                __M_writer(unicode(post.text(teaser_only=True)))
                __M_writer(u'\n')
            else:
                __M_writer(u'    <section class="post-excerpt">\n    ')
                __M_writer(unicode(post.text(teaser_only=False)))
                __M_writer(u'\n')
            __M_writer(u'    </section>\n    <footer class="post-meta">\n')
            if author_pages_generated:
                __M_writer(u'                <a href="')
                __M_writer(unicode(_link('author', post.author())))
                __M_writer(u'">')
                __M_writer(filters.html_escape(unicode(post.author())))
                __M_writer(u'</a>\n')
            else:
                __M_writer(u'                ')
                __M_writer(filters.html_escape(unicode(post.author())))
                __M_writer(u'\n')
            __M_writer(u'\n        on\n')
            for tag in post.tags:
                __M_writer(u'                <a href="link://tag/')
                __M_writer(unicode(tag))
                __M_writer(u'">#')
                __M_writer(unicode(tag))
                __M_writer(u'</a>,\n')
            __M_writer(u'\n        <time class="post-date" datetime="')
            __M_writer(unicode(post.formatted_date('webiso')))
            __M_writer(u'">\n            ')
            __M_writer(filters.html_escape(unicode(post.formatted_date(date_format))))
            __M_writer(u'\n        </time>\n    </footer>\n</article>\n')
        __M_writer(u'</div>\n')
        __M_writer(unicode(helper.html_pager()))
        __M_writer(u'\n')
        __M_writer(unicode(comments.comment_link_script()))
        __M_writer(u'\n')
        __M_writer(unicode(math.math_scripts_ifposts(posts)))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def extra_head():
            return render_extra_head(context)
        permalink = context.get('permalink', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        math = _mako_get_namespace(context, 'math')
        index_file = context.get('index_file', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(unicode(parent.extra_head()))
        __M_writer(u'\n')
        if posts and (permalink == '/' or permalink == '/' + index_file):
            __M_writer(u'        <link rel="prefetch" href="')
            __M_writer(unicode(posts[0].permalink()))
            __M_writer(u'" type="text/html">\n')
        __M_writer(u'    ')
        __M_writer(unicode(math.math_styles_ifposts(posts)))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_header():
            return render_content_header(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"128": 26, "129": 30, "130": 30, "131": 30, "132": 30, "133": 32, "134": 33, "135": 34, "136": 34, "137": 35, "138": 36, "139": 37, "140": 37, "141": 39, "142": 41, "143": 42, "144": 42, "145": 42, "146": 42, "147": 42, "148": 43, "149": 44, "150": 44, "23": 5, "152": 46, "153": 48, "26": 3, "155": 49, "156": 49, "29": 2, "158": 49, "159": 51, "32": 4, "161": 52, "162": 53, "163": 53, "164": 58, "165": 59, "38": 0, "167": 60, "168": 60, "169": 61, "170": 61, "157": 49, "176": 8, "187": 8, "151": 44, "189": 9, "190": 10, "191": 11, "192": 11, "160": 52, "194": 13, "195": 13, "68": 2, "69": 3, "70": 4, "71": 5, "72": 6, "202": 17, "77": 14, "82": 62, "193": 11, "213": 202, "88": 16, "166": 59, "188": 9, "196": 13, "154": 49, "112": 16, "117": 17, "118": 18, "119": 19, "120": 19, "121": 19, "122": 21, "123": 22, "124": 22, "125": 22, "126": 24, "127": 25}, "uri": "index.tmpl", "filename": "themes/canterville/templates/index.tmpl"}
__M_END_METADATA
"""
