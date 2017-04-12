#!/usr/bin/python2
print "content-type: text/html"
print

import cgi,commands,os
data= cgi.FormContent()

data2=data.keys()

dh1=data['hadoop']
dh2=dh1[0]

#ansible user pass variable
ansivar=" ansible_ssh_user=root ansible_ssh_pass=q"

#dh2 have hadoop version : 'hadoop1' or 'hadoop2'
dn1=data['nn']
dn2=dn1[0]
dt1=data['jt']
dt2=dt1[0]
#namenode in : dn2 '' and jobtracker in dt2
varc25=commands.getoutput("sudo rm -rf  /var/www/cgi-bin/nn.txt ")
varc6=commands.getoutput("sudo  touch /var/www/cgi-bin/nn.txt ")
varc5=commands.getoutput("sudo chmod 777 /var/www/cgi-bin/nn.txt ")

varc7=open('nn.txt',mode='a')
varc7.write(dn2+ansivar)
varc7.write("\n")
varc7.close()
varc12=commands.getoutput("sudo  touch /var/www/cgi-bin/allnode.txt ")
varc14=commands.getoutput("sudo chmod 777 /var/www/cgi-bin/allnode.txt ")

varc13=commands.getoutput("sudo cat /var/www/cgi-bin/nn.txt >>/var/www/cgi-bin/allnode.txt ")

varc26=commands.getoutput("sudo rm -rf  /var/www/cgi-bin/jt.txt ")
varc9=commands.getoutput("sudo  touch /var/www/cgi-bin/jt.txt ")
varc10=commands.getoutput("sudo chmod 777 /var/www/cgi-bin/jt.txt ")

varc11=open('jt.txt',mode='a')
varc11.write(dt2+ansivar)
varc11.write("\n")
varc11.close()


varc16=commands.getoutput("sudo cat /var/www/cgi-bin/jt.txt >>/var/www/cgi-bin/allnode.txt ")
varc15=commands.getoutput("sudo chmod 777 /var/www/cgi-bin/allnode.txt ")

data2.remove('nn')
data2.remove('jt')
data2.remove('hadoop')
dd2=data2

data3=len(dd2)

varc27=commands.getoutput("sudo rm -rf  /var/www/cgi-bin/dn.txt ")
varc1=commands.getoutput("sudo  touch /var/www/cgi-bin/dn.txt ")
varc2=commands.getoutput("sudo chmod 777 /var/www/cgi-bin/dn.txt ")


for data4 in range(data3):
	data5=dd2[data4]
	data6 = data5  + ansivar+"\n"
	data7=open('dn.txt',mode='a')
	data7.write(data6)	
	data7.close()
	data4 = data4  + 1

print "<br>"

varc3=commands.getoutput("sudo cat /var/www/cgi-bin/dn.txt >>/var/www/cgi-bin/allnode.txt ")
varc4=commands.getoutput("sudo chmod 777 /var/www/cgi-bin/allnode.txt ")

varcd1=commands.getoutput("sudo  touch /var/www/cgi-bin/check.txt ")
varcd2=commands.getoutput("sudo chmod 777 /var/www/cgi-bin/check.txt ")
varc4=commands.getoutput("sudo cat /var/www/cgi-bin/allnode.txt >>/var/www/cgi-bin/check.txt ")

ggg=commands.getoutput("sudo sshpass -p 'q' scp vimal.py "+dn2+":/var/www/cgi-bin/")
ghhgg=commands.getoutput("sudo sshpass -p 'q' ssh "+dn2+" chmod 777 /var/www/cgi-bin/vimal.py")


#function
if dh2 == 'hadoop1':
	commands.getoutput("sudo ansible all -i /var/www/cgi-bin/allnode.txt  -a 'rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --replacefiles'")
	commands.getoutput("sudo touch /var/www/cgi-bin/core-site.xml")
	commands.getoutput("sudo chown apache  /var/www/cgi-bin/core-site.xml")
	commands.getoutput("sudo touch /var/www/cgi-bin/mapred-site.xml")
	commands.getoutput("sudo chown  apache /var/www/cgi-bin/mapred-site.xml")
	ar1=open('core.xml',mode='r')
	ar2=ar1.read()
	ar3=ar2.replace("nnip",dn2)
	ar1.close()
	ar4=open('core-site.xml',mode='a')
	ar4.write(ar3)
	ar4.close()
        ar11=open('mapred.xml',mode='r')
        ar12=ar11.read()
        ar13=ar12.replace("jtip",dt2)
        ar11.close()
        ar14=open('mapred-site.xml',mode='a')
        ar14.write(ar13)
        ar14.close()
	commands.getoutput("sudo ansible all -i /var/www/cgi-bin/allnode.txt -m copy -a 'src=/var/www/cgi-bin/core-site.xml  dest=/etc/hadoop/'")
	commands.getoutput("sudo ansible all -i /var/www/cgi-bin/jt.txt -m copy -a 'src=/var/www/cgi-bin/mapred-site.xml  dest=/etc/hadoop/'")
	commands.getoutput("sudo ansible all -i /var/www/cgi-bin/dn.txt -m copy -a 'src=/var/www/cgi-bin/mapred-site.xml  dest=/etc/hadoop/'")
	commands.getoutput("sudo ansible all -i /var/www/cgi-bin/nn.txt -m copy -a 'src=/var/www/cgi-bin/hdfs-site.xml  dest=/etc/hadoop/'")
	commands.getoutput("sudo ansible all -i /var/www/cgi-bin/nn.txt -a 'hadoop namenode -format  -force'")
	commands.getoutput("sudo ansible all -i /var/www/cgi-bin/dn.txt -m copy -a 'src=/var/www/hdfs-site.xml  dest=/etc/hadoop/'")
        commands.getoutput("sudo ansible all -i /var/www/cgi-bin/nn.txt -a 'hadoop-daemon.sh start namenode'")
        commands.getoutput("sudo ansible all -i /var/www/cgi-bin/dn.txt -a 'hadoop-daemon.sh start datanode'")
        commands.getoutput("sudo ansible all -i /var/www/cgi-bin/jt.txt -a 'hadoop-daemon.sh start jobtracker'")
        commands.getoutput("sudo ansible all -i /var/www/cgi-bin/dn.txt -a 'hadoop-daemon.sh start tasktracker'")
	commands.getoutput("sudo rm -rf /var/www/cgi-bin/core-site.xml")
	commands.getoutput("sudo rm -rf /var/www/cgi-bin/mapred-site.xml")
else:
	print ""


#delete use txt file
varcde26=commands.getoutput("sudo rm -rf  /var/www/cgi-bin/dn.txt ")
varcde27=commands.getoutput("sudo rm -rf  /var/www/cgi-bin/jt.txt ")
varcde28=commands.getoutput("sudo rm -rf  /var/www/cgi-bin/nn.txt ")
varcde29=commands.getoutput("sudo rm -rf  /var/www/cgi-bin/allnode.txt")

print "Hadoop version  :"+dh2
print "<br>"

print "IP address of Namenode is : "+dn2
print "<br>"
print "IP adsress of Jobtracker is : " + dt2
print "<br>"
print "No of Datanodes or TaskTrackers is  : " + str(data3)
print "<p><b> Your cluster is ready . start using it. </b></p>"

print "<fieldset>"
print "<legend><b> Upload data file to your Cluster</b></legend>"

print "<form  class='c11' action='http://192.168.0.86/cgi-bin/vimal.py' method='post' enctype='multipart/form-data'>"
print "start uploading data "
print "<input name='filename' type='file'  /><br><br>"
print "<input name='data' type='submit' value='upload'  />"
print "</form>"
print "</fieldset>"
