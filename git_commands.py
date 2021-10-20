#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 14:36:21 2021

@author: bszekely

Automate Github bash commands only works for Linux 
"""
import subprocess

def run(*args):
    return subprocess.check_call(['git'] + list(args))

def initialize():
    message = input("do you want to initialize an empty git repo? yes/no")
    if message.lower() == "yes":
        run("init")
    else:
        print("git is already initialized, proceed")

def add():
    message = input("\nDo you want to git add all files or specific? all/specific")
    if message == "all":
        run("add","--all")
    elif message == "specific":
        message2 = input("\nwhat files would you like to input ")
        run(message2)
    
    
if __name__ == '__main__':
    command_prompt = input("input what git command you want")
    command_prompt = command_prompt.lower()
    if command_prompt == "add":
        add()
    elif command_prompt == "init":
        initialize()
