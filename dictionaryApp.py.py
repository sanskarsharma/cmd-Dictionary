import json 
from difflib import get_close_matches

def checkreply(reply):
	reply = reply.lower()
	if(reply == "y" or reply=="yes" or reply[:2]=="yo" or reply[:2]=="ya" or reply[:2]=="yu" or reply=="yep" or reply[:2]=="ha"):
		print("Okay, ")
		return True
	else:
		return False

datadict = json.load(open("data.json"))

flag = True
while(flag):
	print("Enter word to be searched :")
	query = input()
	query = query.lower() # our json file has all keys in lowercase
	if(query in datadict):
		result = datadict[query]
	elif(len(get_close_matches(query,datadict.keys())) > 0):
		query = get_close_matches(query,datadict.keys())[0]
		result = datadict[query]
		print("Did you mean %s instead ? (Y/N)" %query)
		reply = checkreply(str(input()))
		if(not reply):
			print("Than that word does not exist in our dictionary, re-check what you typed.")
			print("Do you want to search for another word ? (Y/N)")
			flag = checkreply(str(input()))
			continue
	else:
		print("That word does not exist in our dictionary")
		print("Do you want to search for another word ? (Y/N)")
		flag = checkreply(str(input()))
		continue


	print("Found "+ str(len(result)) + " results : "+ "\n")

	ans = ""
	count = 1
	for i in result:
		ans = ans + str(count)+". "+ i + "\n"
		count+=1

	print(ans)
	print("Want to search for another word ? (Y/N)")
	flag = checkreply(str(input()))

print("bye.")
	

