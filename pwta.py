# -*- coding: utf-8 -*-

from sys import argv
from subprocess import call

if len(argv) < 2:
	print("Need a password list")
	exit()

scname, plist = argv

OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
CYAN = '\033[96m'
ENDC = '\033[0m'
OJTEST = "\033[38;5;215m"

def cls():
	_tmp = call("clear", shell = True)

LOGO = """
██████╗ ██╗    ██╗████████╗ █████╗ 
██╔══██╗██║    ██║╚══██╔══╝██╔══██╗
██████╔╝██║ █╗ ██║   ██║   ███████║
██╔═══╝ ██║███╗██║   ██║   ██╔══██║
██║     ╚███╔███╔╝   ██║   ██║  ██║
╚═╝      ╚══╝╚══╝    ╚═╝   ╚═╝  ╚═╝
  PassWord Topology Analyzer v0.1
  By: Marcel Goulart P.
"""

legend = """
\033[1m\033[93mU\033[0m = Uppercase       \033[1m\033[96ml\033[0m = Lowercase
\033[1m\033[91mS\033[0m = Special/Symbol  \033[1m\033[92md\033[0m = Digit
"""


cls()
print(OKBLUE + LOGO + ENDC)
print(legend)


with open(plist, 'r') as file:

	for pwd in file:

		temp = pwd.rstrip()

		print(OJTEST + "\nLength: " + OKGREEN + str(len(temp)).zfill(2) + ENDC + " - ", end="")

		for char in temp:

			if char.isalpha():

				if char.isupper():

					print(WARNING + "U" + ENDC, end="")

				elif char.islower():

					print(CYAN + "l" + ENDC, end="")
			else:

				try:

					test = int(char)

				except:

					print(FAIL + "S" + ENDC, end="")

				else:

					print(OKGREEN + "d" + ENDC, end="")

	print("\n")


		
