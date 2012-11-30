#!/usr/bin/env python

"""为命令行工具markdown转换的HTML提供一个易于阅读的外观样式

usage: m2h.py some_markdown_file.md

在当前目录生成一个同名html文件：some_markdown_file.html
"""

import subprocess
from sys import argv

template = """
  <!DOCTYPE HTML>
  <html lang="zh">
  <head>
    <meta charset="UTF-8">
    <title>%s</title>
    <style>
      body {
        font: 0.75em/1.5 "Microsoft Yahei", thoma, arial;
        background-color: #f0f0f0;
      }
      code {
        font-family: Courier;
      }
      .page {
        background-color: #fff;
        border: 1px solid #ccc;
        margin: auto;
        padding: 2em 5em;
        width: 38em;
      }
    </style>
  </head>
  <body>
    <div class="page">
      %s
    </div>
  </body>
  </html>
"""

filename = argv[1]

md = open(filename)
title = md.readline().strip('#').strip()
md.close()

p = subprocess.Popen(['markdown', filename], stdout=subprocess.PIPE,
    stderr=subprocess.PIPE)
outdata, errdata = p.communicate()
if not errdata and outdata:
  html = open(filename.rsplit('.', 1)[0] + '.html', 'w')
  html.write(template % (title, outdata))
  html.close()
else:
  print errdata
