import os
print ("Updating Website...")
#os.remove("index.htm")
head="<html><head><title>
Site </title></head>
<body align='center'><center>
<img src='http://#' width='400px'><br>
<br><div style='color:#ff0000'><strong>
The information that included in the link below is strictly confidential and should not be shared with anyone outside of the Task Force.</strong>
</div><br>"
body=""
for entry in os.listdir('C:///test//'):
    #if entry.is_dir():
        #dir = entry.name
        #print (dir)
    if entry!='web.config'  and entry!='index.htm':
        body='<a href="http://#'+entry+'">'+entry+"</a><br>\n"+body
foot="</body></html>"

var=head+body+foot


filename="C:///test//index.htm"
with open(filename, 'w+') as out:
    out.seek(0)
    out.write(var + '\n')