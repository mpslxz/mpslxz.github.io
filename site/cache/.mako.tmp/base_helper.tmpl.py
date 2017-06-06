# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1496709591.463293
_enable_loop = True
_template_filename = u'themes/canterville/templates/base_helper.tmpl'
_template_uri = u'base_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_translations', 'html_headstart', 'late_load_js', 'html_stylesheets', 'html_feedlinks']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translations(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    <ul class="translations">\n')
        for langname in sorted(translations):
            if langname != lang:
                __M_writer(u'            <li><a href="')
                __M_writer(unicode(abs_link(_link("root", None, langname))))
                __M_writer(u'" rel="alternate" hreflang="')
                __M_writer(unicode(langname))
                __M_writer(u'">')
                __M_writer(unicode(messages("LANGUAGE", langname)))
                __M_writer(u'</a></li>\n')
        __M_writer(u'    </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_headstart(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        prevlink = context.get('prevlink', UNDEFINED)
        url_type = context.get('url_type', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        comment_system = context.get('comment_system', UNDEFINED)
        blog_title = context.get('blog_title', UNDEFINED)
        use_open_graph = context.get('use_open_graph', UNDEFINED)
        title = context.get('title', UNDEFINED)
        url_replacer = context.get('url_replacer', UNDEFINED)
        is_rtl = context.get('is_rtl', UNDEFINED)
        use_base_tag = context.get('use_base_tag', UNDEFINED)
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        extra_head_data = context.get('extra_head_data', UNDEFINED)
        description = context.get('description', UNDEFINED)
        theme_color = context.get('theme_color', UNDEFINED)
        nextlink = context.get('nextlink', UNDEFINED)
        def html_feedlinks():
            return render_html_feedlinks(context)
        meta_generator_tag = context.get('meta_generator_tag', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        favicons = context.get('favicons', UNDEFINED)
        def html_stylesheets():
            return render_html_stylesheets(context)
        twitter_card = context.get('twitter_card', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n<!DOCTYPE html>\n<html ')
        __M_writer(u"prefix='")
        if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']):
            __M_writer(u'og: http://ogp.me/ns# article: http://ogp.me/ns/article# ')
        if comment_system == 'facebook':
            __M_writer(u'fb: http://ogp.me/ns/fb#\n')
        __M_writer(u"' ")
        if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']):
            __M_writer(u'vocab="http://ogp.me/ns" ')
        if is_rtl:
            __M_writer(u'dir="rtl" ')
        __M_writer(u'lang="')
        __M_writer(unicode(lang))
        __M_writer(u'">\n<head>\n    <meta charset="utf-8">\n')
        if use_base_tag:
            __M_writer(u'    <base href="')
            __M_writer(unicode(abs_link(permalink)))
            __M_writer(u'">\n')
        if description:
            __M_writer(u'    <meta name="description" content="')
            __M_writer(filters.html_escape(unicode(description)))
            __M_writer(u'">\n')
        __M_writer(u'    <meta name="viewport" content="width=device-width">\n')
        if title == blog_title:
            __M_writer(u'        <title>')
            __M_writer(filters.html_escape(unicode(blog_title)))
            __M_writer(u'</title>\n')
        else:
            __M_writer(u'        <title>')
            __M_writer(filters.html_escape(unicode(title)))
            __M_writer(u' | ')
            __M_writer(filters.html_escape(unicode(blog_title)))
            __M_writer(u'</title>\n')
        __M_writer(u'\n    ')
        __M_writer(unicode(html_stylesheets()))
        __M_writer(u'\n    <meta name="theme-color" content="')
        __M_writer(unicode(theme_color))
        __M_writer(u'">\n')
        if meta_generator_tag:
            __M_writer(u'    <meta name="generator" content="Nikola (getnikola.com)">\n')
        __M_writer(u'    ')
        __M_writer(unicode(html_feedlinks()))
        __M_writer(u'\n    <link rel="canonical" href="')
        __M_writer(unicode(abs_link(permalink)))
        __M_writer(u'">\n\n')
        if favicons:
            for name, file, size in favicons:
                __M_writer(u'            <link rel="')
                __M_writer(unicode(name))
                __M_writer(u'" href="')
                __M_writer(unicode(file))
                __M_writer(u'" sizes="')
                __M_writer(unicode(size))
                __M_writer(u'"/>\n')
        __M_writer(u'\n')
        if comment_system == 'facebook':
            __M_writer(u'        <meta property="fb:app_id" content="')
            __M_writer(unicode(comment_system_id))
            __M_writer(u'">\n')
        __M_writer(u'\n')
        if prevlink:
            __M_writer(u'        <link rel="prev" href="')
            __M_writer(unicode(prevlink))
            __M_writer(u'" type="text/html">\n')
        if nextlink:
            __M_writer(u'        <link rel="next" href="')
            __M_writer(unicode(nextlink))
            __M_writer(u'" type="text/html">\n')
        __M_writer(u'\n')
        if use_cdn:
            __M_writer(u'        <!--[if lt IE 9]><script src="https://html5shim.googlecode.com/svn/trunk/html5.js"></script><![endif]-->\n')
        else:
            __M_writer(u'        <!--[if lt IE 9]><script src="')
            __M_writer(unicode(url_replacer(permalink, '/assets/js/html5.js', lang, url_type)))
            __M_writer(u'"></script><![endif]-->\n')
        __M_writer(u'\n    ')
        __M_writer(unicode(extra_head_data))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_late_load_js(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'\n    <script type="text/javascript" src="/assets/js/jquery.js"></script>\n    <script type="text/javascript" src="/assets/js/jquery.fitvids.js"></script>\n    <script type="text/javascript" src="/assets/js/index.js"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        needs_ipython_css = context.get('needs_ipython_css', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    <link href="/assets/css/rst.css" rel="stylesheet" type="text/css">\n    <link href="/assets/css/code.css" rel="stylesheet" type="text/css">\n    <link href="/assets/css/theme.css" rel="stylesheet" type="text/css">\n    <link rel="stylesheet" type="text/css" href="/assets/css/screen.css" />\n    <link rel="stylesheet" type="text/css" href="/assets/css/nav.css" />\n    <link rel="stylesheet" type="text/css" href="//fonts.googleapis.com/css?family=Merriweather:300,700,700italic,300italic|Open+Sans:700,400|Inconsolata" />\n')
        if needs_ipython_css:
            __M_writer(u'        <link href="/assets/css/ipython.min.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/nikola_ipython.css" rel="stylesheet" type="text/css">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_feedlinks(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        translations = context.get('translations', UNDEFINED)
        len = context.get('len', UNDEFINED)
        rss_link = context.get('rss_link', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        generate_atom = context.get('generate_atom', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if rss_link:
            __M_writer(u'        ')
            __M_writer(unicode(rss_link))
            __M_writer(u'\n')
        elif generate_rss:
            if len(translations) > 1:
                for language in sorted(translations):
                    __M_writer(u'                <link rel="alternate" type="application/rss+xml" title="RSS (')
                    __M_writer(unicode(language))
                    __M_writer(u')" href="')
                    __M_writer(unicode(_link('rss', None, language)))
                    __M_writer(u'">\n')
            else:
                __M_writer(u'            <link rel="alternate" type="application/rss+xml" title="RSS" href="')
                __M_writer(unicode(_link('rss', None)))
                __M_writer(u'">\n')
        if generate_atom:
            if len(translations) > 1:
                for language in sorted(translations):
                    __M_writer(u'                <link rel="alternate" type="application/atom+xml" title="Atom (')
                    __M_writer(unicode(language))
                    __M_writer(u')" href="')
                    __M_writer(unicode(_link('index_atom', None, language)))
                    __M_writer(u'">\n')
            else:
                __M_writer(u'            <link rel="alternate" type="application/atom+xml" title="Atom" href="')
                __M_writer(unicode(_link('index_atom', None)))
                __M_writer(u'">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 0, "21": 2, "22": 69, "23": 75, "24": 88, "25": 111, "26": 121, "32": 113, "42": 113, "43": 115, "44": 116, "45": 117, "46": 117, "47": 117, "48": 117, "49": 117, "50": 117, "51": 117, "52": 120, "58": 3, "87": 3, "88": 6, "89": 7, "90": 8, "91": 10, "92": 11, "93": 13, "94": 14, "95": 15, "96": 17, "97": 18, "98": 21, "99": 21, "100": 21, "101": 24, "102": 25, "103": 25, "104": 25, "105": 27, "106": 28, "107": 28, "108": 28, "109": 30, "110": 31, "111": 32, "112": 32, "113": 32, "114": 33, "115": 34, "116": 34, "117": 34, "118": 34, "119": 34, "120": 36, "121": 37, "122": 37, "123": 38, "124": 38, "125": 39, "126": 40, "127": 42, "128": 42, "129": 42, "130": 43, "131": 43, "132": 45, "133": 46, "134": 47, "135": 47, "136": 47, "137": 47, "138": 47, "139": 47, "140": 47, "141": 50, "142": 51, "143": 52, "144": 52, "145": 52, "146": 54, "147": 55, "148": 56, "149": 56, "150": 56, "151": 58, "152": 59, "153": 59, "154": 59, "155": 61, "156": 62, "157": 63, "158": 64, "159": 65, "160": 65, "161": 65, "162": 67, "163": 68, "164": 68, "170": 71, "174": 71, "180": 77, "185": 77, "186": 84, "187": 85, "193": 90, "204": 90, "205": 91, "206": 92, "207": 92, "208": 92, "209": 93, "210": 94, "211": 95, "212": 96, "213": 96, "214": 96, "215": 96, "216": 96, "217": 98, "218": 99, "219": 99, "220": 99, "221": 102, "222": 103, "223": 104, "224": 105, "225": 105, "226": 105, "227": 105, "228": 105, "229": 107, "230": 108, "231": 108, "232": 108, "238": 232}, "uri": "base_helper.tmpl", "filename": "themes/canterville/templates/base_helper.tmpl"}
__M_END_METADATA
"""
