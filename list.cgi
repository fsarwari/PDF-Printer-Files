#!/usr/bin/python3


# import OS module
import os, time

# Subfolder of doc-root that contains files
PDF_PATH = 'PDF'

# absolute path of PDF files
path = '/usr/share/cups/doc-root/PDF/'
os.chdir(path)

dir_list = os.listdir('.')
dir_list.sort(key=os.path.getctime)

# change order, newest files first
dir_list=reversed(dir_list)

print("Content-type: text/html\r\n\r\n")

print('''<!DOCTYPE HTML>
<html>
  <head>
    <link rel="stylesheet" href="/cups.css" type="text/css">
    <link rel="shortcut icon" href="/apple-touch-icon.png" type="image/png">
    <meta charset="utf-8">
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=9">
    <meta name="viewport" content="width=device-width">
    <title>PDF Files - CUPS</title>
    <style>
      th, td {
        padding-top: 5px;
        padding-bottom: 5px;
        padding-left: 10px;
        padding-right: 10px;
      }
</style>
  </head>
  <body>
    <div class="header">
      <ul>
	<li><a href="http://www.cups.org/" target="_blank">CUPS.org</a></li>
	<li><a class="active" href="/">Home</a></li>
	<li><a href="/admin">Administration</a></li>
	<li><a href="/list.cgi">PDF Files</a></li>
	<li><a href="/classes/">Classes</a></li>
	<li><a href="/help/">Help</a></li>
	<li><a href="/jobs/">Jobs</a></li>
	<li><a href="/printers/">Printers</a></li>
      </ul>
    </div>
    <div class="body">
''')

print("<h1>PDF-Printer files</h1>")

print('<table cellspacing="0" cellpadding="0">')
print('  <tr><td>Timestamp</td><td>File</td></tr>')
for file in dir_list:
  (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(path + '/' + file)
  print('  <tr>')
  print("    <td>%s</td>" % time.ctime(mtime), end='')

  print('<td><a href="/%s/%s">' % (PDF_PATH,file), end='')
  print('%s</a></td>' % (file), end='')
  print('</tr>')

print('</table>')
print("</body></html>")
