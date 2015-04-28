import re

str1=raw_input()
flag=0
if re.match("[a-zA-Z0-9]+", str1) and len(str1) > 0 and len(str1)<=64:
    if len(str1)>=10 and re.search("[0-9]+",str1) and re.search("[A-Z]+",str1) and re.search("[a-z]+",str1):
        print "True"
    else:
        print "False"
