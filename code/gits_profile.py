import os
import sys
import subprocess
import re

def gits_set_profile(args):
    """
    Function that prints hello message
    to user console
    """
    print(args.email)
    print("Hello from GITS Commandline Tools-Profile")
    check_val = check(args.email) 
    #print(check_val) 
    if check_val == True:  
    	subprocess.call(["git config --global --unset user.name"], shell=True)    
    	subprocess.call(["git config --global --unset user.email"], shell=True)
        #check regex

    	cmd = "git config --global user.email " + args.email
    	print(cmd)
    	subprocess.call([cmd], shell=True)

    	cmd = "git config --global user.name " + args.name
    	print(cmd)
    	subprocess.call([cmd], shell=True)
    
    	verify_email = subprocess.call(["git config --list | grep \"user.email\""], shell = True)   
    	print(verify_email)
    	#add if-else
    	verify_name = subprocess.call(["git config --list | grep \"user.name\""], shell = True) 
    	#print(verify_name)
    	
    else:
        print("Enter a valid email id")






# Define a function for 
# for validating an Email 
def check(email):  

    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
# for custom mails use: '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
  
    # pass the regular expression 
    # and the string in search() method 
    if(re.search(regex,email)):  
        return True
    else:  
        return False
