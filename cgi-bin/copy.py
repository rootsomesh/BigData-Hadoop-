#!/usr/bin/python2
print "content-type: text/html"
print

import cgi,commands,os
vr1=commands.getoutput("nmap -sP 192.168.0.2-255 -n|grep 'Nmap scan'|awk '{print $5}'")
vr2=vr1.replace('\n',' ')
print vr2
vr3=vr2.rsplit()
va1=vr3[:4]
vb1=vr3[4:8]
vc1=vr3[8:]
vr4=len(vr3)
va2=len(va1)
vb2=len(vb1)
vc2=len(vc1)
print "<style>"
print "form.c1"
print "{"
print "border:0px;"
print "width:100%px;"
print "}"
print "input.c2"
print "{"
print "border:5px solid grey;"
print "}"
print "</style>"

print "<fieldset>"
print "<legend>All Avialable Resources</legend>"
print "<form class='c1' action='http://192.168.0.1/cgi-bin/return.py'>"
print "<br>"
print "<br>"

print "<fieldset>"
print "<legend>Select NameNode IP Address</legend>"
for vt in range(va2):
        va11=va1[vt]
        uu=commands.getoutput("sudo  sshpass -p 'q' ssh "+va11+" lscpu | grep '^CPU(s):' |awk '{print$2}'")
        uu=commands.getoutput("sudo  sshpass -p 'q' ssh "+va11+" lscpu | grep '^CPU(s):' |awk '{print$2}'")
        vv=commands.getoutput("sudo  sshpass -p 'q' ssh "+va11+" free -m |grep '^Mem'|awk '{print$4}'")
        print  "ip=" + va11 + " cpu=" + uu +" Free RAM="+vv+"MB" + " <input  name='bbb' value="+va11+ " type='radio'>" + "<br>"
        vt=vt+1
print "</fieldset>"
print "<br>"
print "<br>"

print "<fieldset>"
print "<legend>Select Task Tracker IP Address</legend>"
for vf in range(vb2):
        vs11=vb1[vf]
        uu1=commands.getoutput("sudo  sshpass -p 'q' ssh "+vs11+" lscpu | grep '^CPU(s):' |awk '{print$2}'")
        uu1=commands.getoutput("sudo  sshpass -p 'q' ssh "+vs11+" lscpu | grep '^CPU(s):' |awk '{print$2}'")
        vv1=commands.getoutput("sudo  sshpass -p 'q' ssh "+vs11+" free -m |grep '^Mem'|awk '{print$4}'")
        print  "ip=" + vs11 + " cpu=" + uu1 +" Free RAM="+vv1+"MB" + " <input  name='ccc' value="+vs11+ " type='radio'>" + "<br>"
        vf=vf+1
print "</fieldset>"

print "<br>"
print "<br>"

#vr=0
print "<fieldset>"
print "<legend>Select Datanodes/JobTackers IP Addresses</legend>"
for vr in range(vc2):
	vr11=vc1[vr]
	uu2=commands.getoutput("sudo  sshpass -p 'q' ssh "+vr11+" lscpu | grep '^CPU(s):' |awk '{print$2}'")
	uu2=commands.getoutput("sudo  sshpass -p 'q' ssh "+vr11+" lscpu | grep '^CPU(s):' |awk '{print$2}'")
	vv2=commands.getoutput("sudo  sshpass -p 'q' ssh "+vr11+" free -m |grep '^Mem'|awk '{print$4}'")
	print  "ip=" + vr11 + " cpu=" + uu2 +" Free RAM="+vv2+"MB" + " <input  name="+vr11+" type='checkbox'>" + "<br>"
	vr=vr+1
print "</fieldset>"

print "<br>"
print "<br>"

print "<input type='submit'>" + "<br>"
print " </form> "
print "</fieldset>"
