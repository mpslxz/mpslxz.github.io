# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1504760524.42025
_enable_loop = True
_template_filename = u'/Users/mehran/anaconda2/lib/python2.7/site-packages/nikola/data/themes/base/templates/math_helper.tmpl'
_template_uri = u'math_helper.tmpl'
_source_encoding = 'ascii'
_exports = ['math_scripts', 'math_styles', 'math_styles_ifposts', 'math_styles_ifpost', 'math_scripts_ifpost', 'math_scripts_ifposts']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_math_scripts(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        mathjax_config = context.get('mathjax_config', UNDEFINED)
        use_katex = context.get('use_katex', UNDEFINED)
        katex_auto_render = context.get('katex_auto_render', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if use_katex:
            __M_writer(u'        <script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.7.1/katex.min.js" integrity="sha384-/y1Nn9+QQAipbNQWU65krzJralCnuOasHncUFXGkdwntGeSvQicrYkiUBwsgUqc1" crossorigin="anonymous"></script>\n        <script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.7.1/contrib/auto-render.min.js" integrity="sha256-ExtbCSBuYA7kq1Pz362ibde9nnsHYPt6JxuxYeZbU+c=" crossorigin="anonymous"></script>\n')
            if katex_auto_render:
                __M_writer(u'            <script>\n                renderMathInElement(document.body,\n                    {\n                        ')
                __M_writer(unicode(katex_auto_render))
                __M_writer(u'\n                    }\n                );\n            </script>\n')
            else:
                __M_writer(u'            <script>\n                renderMathInElement(document.body);\n            </script>\n')
        else:
            __M_writer(u'        <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS-MML_HTMLorMML" integrity="sha256-yYfngbEKv4RENfGDvNUqJTqGFcKf31NJEe9OTnnMH3Y=" crossorigin="anonymous"></script>\n')
            if mathjax_config:
                __M_writer(u'        ')
                __M_writer(unicode(mathjax_config))
                __M_writer(u'\n')
            else:
                __M_writer(u'        <script type="text/x-mathjax-config">\n        MathJax.Hub.Config({tex2jax: {inlineMath: [[\'$latex \',\'$\'], [\'\\\\(\',\'\\\\)\']]}});\n        </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_math_styles(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        use_katex = context.get('use_katex', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if use_katex:
            __M_writer(u'        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.7.1/katex.min.css" integrity="sha384-wITovz90syo1dJWVh32uuETPVEtGigN07tkttEqPv+uR2SE/mbQcG7ATL28aI9H0" crossorigin="anonymous">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_math_styles_ifposts(context,posts):
    __M_caller = context.caller_stack._push_frame()
    try:
        def math_styles():
            return render_math_styles(context)
        any = context.get('any', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if any(post.is_mathjax for post in posts):
            __M_writer(u'    ')
            __M_writer(unicode(math_styles()))
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_math_styles_ifpost(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        def math_styles():
            return render_math_styles(context)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if post.is_mathjax:
            __M_writer(u'    ')
            __M_writer(unicode(math_styles()))
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_math_scripts_ifpost(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        def math_scripts():
            return render_math_scripts(context)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if post.is_mathjax:
            __M_writer(u'    ')
            __M_writer(unicode(math_scripts()))
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_math_scripts_ifposts(context,posts):
    __M_caller = context.caller_stack._push_frame()
    try:
        def math_scripts():
            return render_math_scripts(context)
        any = context.get('any', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if any(post.is_mathjax for post in posts):
            __M_writer(u'    ')
            __M_writer(unicode(math_scripts()))
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"130": 42, "131": 43, "132": 44, "133": 44, "134": 44, "140": 134, "16": 0, "21": 28, "22": 34, "23": 40, "24": 46, "25": 52, "26": 58, "32": 1, "39": 1, "40": 2, "41": 3, "42": 5, "43": 6, "44": 9, "45": 9, "46": 13, "47": 14, "48": 18, "49": 19, "50": 20, "51": 21, "52": 21, "53": 21, "54": 22, "55": 23, "61": 30, "66": 30, "67": 31, "68": 32, "74": 54, "81": 54, "82": 55, "83": 56, "84": 56, "85": 56, "91": 48, "97": 48, "98": 49, "99": 50, "100": 50, "101": 50, "107": 36, "113": 36, "114": 37, "115": 38, "116": 38, "117": 38, "123": 42}, "uri": "math_helper.tmpl", "filename": "/Users/mehran/anaconda2/lib/python2.7/site-packages/nikola/data/themes/base/templates/math_helper.tmpl"}
__M_END_METADATA
"""
