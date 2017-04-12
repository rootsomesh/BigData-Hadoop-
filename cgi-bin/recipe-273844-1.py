#!/usr/bin/python2
print "content-type: text/html"
print


"""This demonstrates a minimal http upload cgi.
This allows a user to upload up to three files at once.
It is trivial to change the number of files uploaded.

This script has security risks. A user could attempt to fill
a disk partition with endless uploads. 
If you have a system open to the public you would obviously want
to limit the size and number of files written to the disk.
"""
import cgi
import cgitb; cgitb.enable()
import os, sys

upload_dir = "/ff"

form = cgi.FieldStorage()
print form
print "<br>"
name=form["file_1"]
#print name.filename
name1 = name.filename
#print "<br>"
#print dir(name)
#name.make_file("/ff/",)


fout = file (os.path.join(upload_dir, name1), 'wb')
print "<br>"
print done
while 1:
	chunk = name.file.read(100000)
	open(fout,mode='a')
	fout.write (chunk)
	fout.close()

