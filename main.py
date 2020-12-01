import os
from pypinyin import pinyin
import re
import pdfkit

from jinja2 import Template

g_cur_path = os.path.dirname(os.path.abspath(__file__))

def wash(name='input.txt'):
    
    file = os.path.join(g_cur_path, name)
    with open(file, 'r', encoding='utf-8') as rh:
        lines = rh.read()
        lines = re.sub('\n', '', lines)
        lines = re.sub('\s+\[', '.', lines)
        lines = re.sub('\]', '', lines)
        lines = re.sub('译文对照', '', lines)
        return lines.split('$')

def gen_pinyin(line):
    py = pinyin(line, errors='ignore')
    py = [i[0] for i in py]
    return line, py

def render_one_line(line, py):
    max_mum_length = 18
    template = Template('''
            <tr>
                {% for item in py %}
                    <td> {{ item }} </td>
                {% endfor %}
            </tr>
            <tr>
                {% for item in line %}
                    <td> {{ item }} </td>
                {% endfor %}
            </tr>
        ''')
    total = []
    while len(line) > max_mum_length:
        a = line[:max_mum_length]
        b = py[:max_mum_length]
        total.append(template.render(line=a, py=b))
        line = line[max_mum_length:]
        py = py[max_mum_length:]
    if len(line):
        total.append(template.render(line=line, py=py))
    return '\n'.join(total)

def reader_one_poem(poem):
    template = Template('''
        <table>
            {{ content }}
        </table>
    ''')
    poem = poem.replace('===', '\n')
    poem = re.sub('【', '\n', poem, count=1)
    poem = poem.replace('【', '')
    # poem = poem.replace('[', '')
    # poem = poem.replace(']', '')
    poem = poem.replace('、', '')
    poem = poem.replace('】', '') 
    poem = poem.replace('。','。\n') 
    poem = poem.replace('？','。\n') 
    poem_pieces = poem.split('\n')
    poem_pieces = [a.strip() for a in poem_pieces if a.strip()]
    all = []
    for line in poem_pieces:
        py = pinyin(line)
        py = [i[0] for i in py]
        all.append(render_one_line(line, py))
    return template.render(content='\n'.join(all))
    

def gen_pdf(content, name="out.pdf"):
    pdfkit.from_string(content, os.path.join(g_cur_path, 'out.pdf'))


def gen_html(lines):
    all = []
    for line in lines:
       a = reader_one_poem(line)
       all.append(a)
    file = os.path.join(g_cur_path, "templete.html")
    with open(file, 'r', encoding='utf-8') as rh:
        template = Template(rh.read())
    render_html = template.render(content='<hr />'.join(all))
    with open(os.path.join(g_cur_path, 'out.html'), 'w', encoding='utf-8') as wh:
        wh.write(render_html)

    gen_pdf(render_html)

if __name__ == "__main__":
    o = wash()
    gen_html(o)
