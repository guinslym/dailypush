#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import os

___author__= 'Guinsly Mondesir'

def command_line(cmd):
    """[summary]
    
    [description]
    
    Arguments:
        cmd {[list]} -- a list that represent the command that 
        we will pass to the shell (Terminal)
    
    Returns:
        [type] -- raise a ValueError if you didn't pass the correct command
    """
    try:
        s = subprocess.check_output(cmd)
        return s.strip()
    except subprocess.CalledProcessError:
        raise ValueError('An error occurs with the command that you passed.')

#Change to the current directory
def cd_to_this_file_directory():
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

cd_to_this_file_directory()

with open('README.md', 'a') as myfile:
    myfile.write(' .')

sentences = [
  'git add *',
  'git commit -m New-changes',
  'git push origin master'
  ]

for cmd in sentences:
    command_line(cmd.split())



