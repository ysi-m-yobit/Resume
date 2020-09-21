import markdown
import os
import re

def ToVueComponent(html:str):
    return """\
<template>
<div class="base">
<div class="container">""" + html + """\
</div>
</div>
</template>"""

def ConvertMaterialTags(html:str):
    """
    plane tag only. example:<li> <p>
    """
    return html.replace('<ul>','<ul class="collection">')\
        .replace('<li>','<li class="collection-item">')\
        .replace('<table>','<table class="striped centered">')\
        .replace('<p>','<p class="card-panel blue lighten-5">')

def ConvertDelighterTags(html:str):
    replaced_html = html.replace('<ul>','<ul data-delighter>')\
        # .replace('<h3>','<h3 class="deright" data-delighter>')\
        .replace('<h5>','<h5 class="h5" data-delighter>')\
        # .replace('<p>','<p class="deleft" data-delighter>')

    replaced_html = re.sub('(?!.*data-delighter)<ul.*(class="[^"]*).*?>','<ul \\1" data-delighter>', replaced_html)
    # replaced_html = re.sub('(?!.*data-delighter)<h3.*(class="[^"]*).*?>','<h3 \\1 deright" data-delighter>', replaced_html)
    replaced_html = re.sub('(?!.*data-delighter)<h5.*(class="[^"]*).*?>','<h5 \\1 h5" data-delighter>', replaced_html)
    # replaced_html = re.sub('(?!.*data-delighter)<p.*(class="[^"]*).*?>','<p \\1 deleft" data-delighter>', replaced_html)

    return replaced_html

def AllConvert():
    current_dir = os.path.dirname(__file__)
    src_path = os.path.join(current_dir, '../../README.md')
    dst_path = os.path.join(current_dir, '../../js/src/vue/ResumeBody.vue')

    with open(src_path, 'r', encoding="utf-8_sig") as open_src, open(dst_path, 'w',encoding="utf-8_sig") as open_dst:
        html = markdown.markdown(open_src.read(), extensions=['codehilite', 'tables', 'attr_list'])
        vue_component_html = ToVueComponent(html)
        materiarized_html = ConvertMaterialTags(vue_component_html)
        delighted_html = ConvertDelighterTags(materiarized_html)
        
        open_dst.write(delighted_html)