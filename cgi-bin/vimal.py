#!/usr/bin/python2
print "content-type: text/html"
print

import cgi,commands,os
import cgitb; cgitb.enable()
form = cgi.FieldStorage()
fileitem=form['filename']
fn= os.path.basename(fileitem.filename)
open('/hadoop/'+fn,'wb').write(fileitem.file.read())
var = fileitem.filename


nn=commands.getoutput("sudo hadoop fs -chmod -R 777 /tmp ")
mm=commands.getoutput("sudo hadoop fs -put /hadoop/"+var+"  / ")
print "done"

