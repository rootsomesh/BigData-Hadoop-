#!/usr/bin/python2
print "content-type: text/html"
print

import cgi,commands,os,sys
import cgitb; cgitb.enable()
form = cgi.FieldStorage()

hh=form.getvalue('hello')
fileitem = form['hello']

fout = file (os.path.join(/ff/,hh), 'wb')
while 1:
	chuck = hh.file.read(100000000)
	if not chunk: break
	fout.write (chunk)
fout.close()

print "done"

"""
form_field='hello'
fileitem= form[form_field]
print fileitem 
gg = fileitem.filename
print gg




#form.make_file(self,binary=None)
#print form

t=dir(form)
print t
print form.type()
print gg
hh=form.getvalue('hello')
print hh

aa=dir(hh)
print aa

#commands.getoutput("sudo  cp " form.file(hh) " /root/")

#print "hello"

##print t



bb=type(x.getvalue('hello'))
print bb
print
data=cgi.FormContent()
print data

st1=cgi.FieldStorage()
var=type(st1)
print var
#commands.getoutput('sudo cp -rf' st1  '/root/')
"""
