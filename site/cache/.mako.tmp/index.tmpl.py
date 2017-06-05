# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1496695943.392066
_enable_loop = True
_template_filename = u'/Users/mehran/anaconda2/lib/python2.7/site-packages/nikola/data/themes/base/templates/index.tmpl'
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
        _link = context.get('_link', UNDEFINED)
        front_index_header = context.get('front_index_header', UNDEFINED)
        index_file = context.get('index_file', UNDEFINED)
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        def content_header():
            return render_content_header(context._locals(__M_locals))
        comments = _mako_get_namespace(context, 'comments')
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
        site_has_comments = context.get('site_has_comments', UNDEFINED)
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
        site_has_comments = context.get('site_has_comments', UNDEFINED)
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
            __M_writer(u'    <article class="h-entry post-')
            __M_writer(unicode(post.meta('type')))
            __M_writer(u'">\n    <header>\n        <h1 class="p-name entry-title"><a href="')
            __M_writer(unicode(post.permalink()))
            __M_writer(u'" class="u-url">')
            __M_writer(filters.html_escape(unicode(post.title())))
            __M_writer(u'</a></h1>\n        <div class="metadata">\n            <p class="byline author vcard"><span class="byline-name fn" itemprop="author">\n')
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
            __M_writer(u'            </span></p>\n            <p class="dateline"><a href="')
            __M_writer(unicode(post.permalink()))
            __M_writer(u'" rel="bookmark"><time class="published dt-published" datetime="')
            __M_writer(unicode(post.formatted_date('webiso')))
            __M_writer(u'" title="')
            __M_writer(filters.html_escape(unicode(post.formatted_date(date_format))))
            __M_writer(u'">')
            __M_writer(filters.html_escape(unicode(post.formatted_date(date_format))))
            __M_writer(u'</time></a></p>\n')
            if not post.meta('nocomments') and site_has_comments:
                __M_writer(u'                <p class="commentline">')
                __M_writer(unicode(comments.comment_link(post.permalink(), post._base_path)))
                __M_writer(u'\n')
            __M_writer(u'        </div>\n    </header>\n')
            if index_teasers:
                __M_writer(u'    <div class="p-summary entry-summary">\n    ')
                __M_writer(unicode(post.text(teaser_only=True)))
                __M_writer(u'\n')
            else:
                __M_writer(u'    <div class="e-content entry-content">\n    ')
                __M_writer(unicode(post.text(teaser_only=False)))
                __M_writer(u'\n')
            __M_writer(u'    </div>\n    </article>\n')
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
{"source_encoding": "utf-8", "line_map": {"128": 24, "129": 25, "130": 26, "131": 26, "132": 26, "133": 28, "134": 28, "135": 28, "136": 28, "137": 31, "138": 32, "139": 32, "140": 32, "141": 32, "142": 32, "143": 33, "144": 34, "145": 34, "146": 34, "147": 36, "148": 37, "149": 37, "150": 37, "23": 5, "152": 37, "153": 37, "26": 3, "155": 37, "156": 38, "29": 2, "158": 39, "159": 39, "32": 4, "161": 43, "162": 44, "163": 45, "164": 45, "165": 46, "38": 0, "167": 48, "168": 48, "169": 50, "170": 53, "171": 54, "172": 54, "173": 55, "174": 55, "157": 39, "176": 56, "200": 13, "182": 8, "201": 13, "151": 37, "193": 8, "198": 11, "160": 41, "175": 56, "195": 9, "196": 10, "69": 2, "70": 3, "71": 4, "72": 5, "73": 6, "202": 13, "78": 14, "208": 17, "83": 57, "197": 11, "89": 16, "219": 208, "199": 11, "166": 47, "194": 9, "154": 37, "114": 16, "119": 17, "120": 18, "121": 19, "122": 19, "123": 19, "124": 21, "125": 22, "126": 22, "127": 22}, "uri": "index.tmpl", "filename": "/Users/mehran/anaconda2/lib/python2.7/site-packages/nikola/data/themes/base/templates/index.tmpl"}
__M_END_METADATA
"""
