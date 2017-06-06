# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1496709591.3289
_enable_loop = True
_template_filename = u'/Users/mehran/anaconda2/lib/python2.7/site-packages/nikola/data/themes/base/templates/pagination_helper.tmpl'
_template_uri = u'pagination_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['page_navigation']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_navigation(context,current_page,page_links,prevlink,nextlink,prev_next_links_reversed,surrounding=5):
    __M_caller = context.caller_stack._push_frame()
    try:
        abs = context.get('abs', UNDEFINED)
        len = context.get('len', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n<div class="page-navigation">\n')
        for i, link in enumerate(page_links):
            if abs(i - current_page) <= surrounding or i == 0 or i == len(page_links) - 1:
                if i == current_page:
                    __M_writer(u'        <span class="current-page">')
                    __M_writer(unicode(i+1))
                    __M_writer(u'</span>\n')
                else:
                    __M_writer(u'        <a href="')
                    __M_writer(unicode(page_links[i]))
                    __M_writer(u'">')
                    __M_writer(unicode(i+1))
                    __M_writer(u'</a>\n')
            elif i == current_page - surrounding - 1 or i == current_page + surrounding + 1:
                __M_writer(u'      <span class="ellipsis">\u2026</span>\n')
        __M_writer(u'</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"48": 12, "34": 2, "35": 4, "36": 5, "37": 6, "38": 7, "39": 7, "40": 7, "41": 8, "42": 9, "43": 9, "44": 9, "45": 9, "46": 9, "47": 11, "16": 0, "49": 15, "21": 16, "55": 49, "27": 2}, "uri": "pagination_helper.tmpl", "filename": "/Users/mehran/anaconda2/lib/python2.7/site-packages/nikola/data/themes/base/templates/pagination_helper.tmpl"}
__M_END_METADATA
"""
