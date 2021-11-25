import re
f=open("test.txt","r+")
txt=f.read()
emailids=txt.split("\n")
fi=open("invaild.txt","w+")
fv=open("vaild.txt","w+")
for email in emailids:
    if re.match(r'(.*)@(.*).com',email):
        fv.write(email+"\n")
    else:
        fi.write(email+"\n")
        
