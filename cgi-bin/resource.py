#!/usr/bin/python2
print "content-type: text/html"
print

import cgi,commands,os

print "<br>"
print "<br>"
varc51=commands.getoutput("sudo  touch /var/www/cgi-bin/check.txt ")
varc52=commands.getoutput("sudo chmod 777 /var/www/cgi-bin/check.txt ")
tx1=open('check.txt',mode='r')
tx2=tx1.read()
tx1.close()
tx3=tx2.replace("\n"," ")
tx4=tx3.split()
c=tx4

vr1=commands.getoutput("sudo nmap -sP 192.168.0.2-255 -n|grep 'Nmap scan'|awk '{print $5}'")
vr2=vr1.replace('\n',' ')

vr3=vr2.rsplit()
####
n=vr3
s=0
while s<255:
	if s == len(n):
		break
	else:
		if n[s] in c:
			n.remove(n[s])
			s=s-1
		else:
			print ""
	s=s+1

tx4=c
vr3=n
##############
va1=vr3[:3]
vb1=vr3[3:6]


vc1=vr3[6:]
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

#varc51=commands.getoutput("sudo  touch /var/www/cgi-bin/check.txt ")
#varc52=commands.getoutput("sudo chmod 777 /var/www/cgi-bin/check.txt ")


print "<fieldset>"
print "<legend><h3>All Avialable Resources</h3></legend>"
print "<form class='c1' action='http://192.168.0.1/cgi-bin/return.py'>"
print "<br>"
print "<br>"

print "<style>"
print "fieldset.field1"
print "{"
print "padding-left:50px;"
print "}"
print "</style>"
print "<fieldset class='field1'>"
print "<legend><b>Select Apache hadoop version </b></legend>" + "<br>"
var91="hadoop1"
var92="hadoop2"
print  "<b><t>Hadoop Version</t> </b>"+ "<br>"

print  "Apache "+ var91 + " <input  name='hadoop' value="+var91+ "  type='radio'>" 
print  "Apache "+ var92 +" <input  name='hadoop' value="+var92+ "  type='radio'>" + "<br>"
print "</fieldset>"

print "<br>"
print "<br>"

print "<fieldset>"
print "<legend><b>Select NameNode IP Address</b></legend>"
for vt in range(va2):
        va11=va1[vt]
	uu=commands.getoutput("sudo  sshpass -p 'q' ssh "+va11+" lscpu | grep '^CPU(s):' |awk '{print$2}'")
        uu=commands.getoutput("sudo  sshpass -p 'q' ssh "+va11+" lscpu | grep '^CPU(s):' |awk '{print$2}'")
        vv=commands.getoutput("sudo  sshpass -p 'q' ssh "+va11+" free -m |grep '^Mem'|awk '{print$4}'")
	ww=commands.getoutput("sudo  sshpass -p 'q' ssh "+va11+" df -hT |grep 'data'|awk '{print$5}'")

        print  "IP=" + va11 + " cpu=" + uu +" Free RAM="+vv+"MB"  +" Free Space="+ww+"GB"+ " <input  name='nn' value="+va11+ " type='radio'>" + "<br>"
        vt=vt+1
print "</fieldset>"
print "<br>"
print "<br>"

print "<fieldset>"
print "<legend><b>Select Job Tracker IP Address</b></legend>"
for vf in range(vb2):
        vs11=vb1[vf]
	uu1=commands.getoutput("sudo  sshpass -p 'q' ssh "+vs11+" lscpu | grep '^CPU(s):' |awk '{print$2}'")
        uu1=commands.getoutput("sudo  sshpass -p 'q' ssh "+vs11+" lscpu | grep '^CPU(s):' |awk '{print$2}'")
        vv1=commands.getoutput("sudo  sshpass -p 'q' ssh "+vs11+" free -m |grep '^Mem'|awk '{print$4}'")
	ww1=commands.getoutput("sudo  sshpass -p 'q' ssh "+vs11+" df -hT |grep 'data'|awk '{print$5}'")
        print  "IP=" + vs11 + " cpu=" + uu1 +" Free RAM="+vv1+"MB"  +" Free Space="+ww1+"GB"+ " <input  name='jt' value="+vs11+ " type='radio'>" + "<br>"
        vf=vf+1
print "</fieldset>"

print "<br>"
print "<br>"

#vr=0
print "<fieldset>"
print "<legend><b>Select Datanodes/TaskTackers IP Addresses</b></legend>"
for vr in range(vc2):
	vr11=vc1[vr]
	uu2=commands.getoutput("sudo  sshpass -p 'q' ssh "+vr11+" lscpu | grep '^CPU(s):' |awk '{print$2}'")
	uu2=commands.getoutput("sudo  sshpass -p 'q' ssh "+vr11+" lscpu | grep '^CPU(s):' |awk '{print$2}'")
	vv2=commands.getoutput("sudo  sshpass -p 'q' ssh "+vr11+" free -m |grep '^Mem'|awk '{print$4}'")
	ww2=commands.getoutput("sudo  sshpass -p 'q' ssh "+vr11+" df -hT |grep 'data'|awk '{print$5}'")
	print  "IP=" + vr11 + " cpu=" + uu2 +" Free RAM="+vv2+"MB" +" Free Space="+ww2+"GB"+" <input  name="+vr11+" type='checkbox'>" + "<br>"
	vr=vr+1
print "</fieldset>"

print "<br>"
print "<br>"

print "<input type='submit' />" 
print "<input type='reset' />" + "<br>"
print " </form> "
print "</fieldset>"
