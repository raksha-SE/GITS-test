import os
import sys
import argparse
from gits_rebase import gits_rebase

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

gits_pr_subparser= subparsers.add_parser('rebase', help='sync help')
gits_pr_subparser.set_defaults(func=gits_rebase)
args = parser.parse_args()
args.func(args)              
