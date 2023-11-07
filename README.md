# PDF-Printer-Files
Browse PDF files created by CUPS-PDF

## Description
Add an additional Section to CUPS PDF webserver to download documents printed to PDF printer.
Added a python CGI program to existing webserver that lists PDFs generated by CUPS-PDF printer and allows you to download them.


## Screenshot
<img src="PDF-Files-screenshot.png" alt="screenshot"  width="300"/>

## Instructions

### Install cups PDF driver
`apt-get install printer-driver-cups-pdf`

### Add list.cgi file 
Copy list.cgi to document-root of cups webserver usually in /usr/share/cups/doc-root
Location will be in /etc/cups/cups-files.conf:#DocumentRoot
Make list.cgi executable `chmod +x list.cgi`

### Embed link into existing CUPS web interface
* in /usr/share/cups/doc-root/index.html line 18 add: `<li><a href="/list.cgi">PDF Files</a></li>`
* in /usr/share/cups/templates/header.tmpl line 35 add: `<li><a href="/list.cgi">PDF Files</a></li>`

### create file /etc/cups/cgi.types
Content:
```application/x-httpd-cgi cgi```

### Modify config in /etc/cups/cups-pdf.conf
```
AnonUMask 0022
UserUMask 0022
Out /usr/share/cups/doc-root/PDF
AnonDirName /usr/share/cups/doc-root/PDF
```

### Delete older files older than one day
`1 1 * * * /usr/bin/find /usr/share/cups/doc-root/PDF -mtime +1 -exec rm {} \;`
