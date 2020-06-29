import json
import sys

arg=sys.argv

with open('package.json', "r") as f:
	data=json.load(f)

# 1st argument is the version of the current package
data['version']=arg[1]

# Setting dependencies versions
if len(arg)>=4:
	for i in range (2,len(arg),2):
		data['dependencies'][arg[i]]=arg[i+1]

with open('package.json', "w") as f:
	json.dump(data,f)
