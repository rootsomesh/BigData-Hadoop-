#!/usr/bin/python2
print "content-type: text/html"
print

import cgi,commands,os
data= cgi.FormContent()

var2=data['cmdinput'][0]
print var2
"""
var1= "sudo "
#print var1 + var2 + "\n"
var3=commands.getoutput( var1 + var2 )
print var3
print "<pre><p><b> \n ok you are done with this</b></p></pre>"
"""
