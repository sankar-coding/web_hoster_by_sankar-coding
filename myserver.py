#!/usr/bin/python

black = '\033[1;30m'
red = '\033[1;31m'
green = '\033[1;32m'
yellow = '\033[1;33m'
blue = '\033[1;34m'
magenta = '\033[1;35m'
cyan = '\033[1;36m'
white = '\033[1;37m'
reset = '\033[0m'

def author():
  print(f"{green}	  _   _")
  print(f"{blue}       	/ \ / \ {cyan} 	+-+-+-+-+-+-+")
  print(f"{magenta}      	( b | y ) 	{yellow}|{green}s{yellow}|{green}a{yellow}|{green}n{yellow}|{green}k{yellow}|{green}a{yellow}|{green}r{yellow}|")
  print(f"{red}         \_/ \_/{cyan}        +-+-+-+-+-+-+")
def title():
  os.system('clear')
  print(f"{cyan}  _____")
  print(f"{red}  / ___/      ________  ______   _____  _____")
  print(f"{green}  \__ \______/ ___/ _ \/ ___/ | / / _ \/ ___/")
  print(f"{magenta} ___/ /_____(__  )  __/ /   | |/ /  __/ /")
  print(f"{yellow}/____/     /____/\___/_/    |___/\___/_/")

#Masseges icon
success = f"{green} [{white}✓{green}] {white}"
getinput = f" {magenta}[{white}+{magenta}] {white}"
dot = f"{yellow} [{white}•{yellow}] {white}"
error = f"{red} [{white}✗{red}] {white}"
alert = f" {blue}[{red}⚠{blue}] {white}"
info = f" {white}[{green}𝑖{white}] "

import os
pwd = os.getcwd()
home_path = os.path.expanduser("~")
#greetings
title()
author()
print(f"{dot}{cyan}Wellcome to S_server \n")
print(f"{success}Select one ..")
print(f"{alert}")

#os.system("apachectl")
#print("http://localhost:8080")
