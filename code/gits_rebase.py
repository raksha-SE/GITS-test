import os
import sys
import subprocess
import argparse

def gits_rebase(args):
    print(args)
    print("Hello from GITS command line tools- Rebase")

    print("Is the rebase on current branch?")
    inp = input("[yes/no][y/n]")
    if inp.lower() == "yes" or inp.lower() == "y"
        rc = os.popen("git rebase master").read()
        print(rc)
    else:
        inp2 =input("Enter the name of the branch you want to rebase")
        print(inp2)
        rc2 = os.popen("git branch | grep "+inp2).read()
        if rc2 == inp2 :
            rc3 = os.popen("git checkout "+inp2+" git rebase master").read()
            print(rc3)
            


