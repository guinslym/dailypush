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
        [ERROR] -- raise a ValueError if you didn't pass the correct command
        [list] -- return a 1 lenght string representing that the
                  script passed
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

def append_to_file():
    with open('README.md', 'a') as myfile:
        myfile.write(' .')

def execute_commands(sentences):
    for cmd in sentences:
        command_line(cmd.split())


if __name__ == '__main__':
    cd_to_this_file_directory()
    append_to_file()
    sentences = ['git add *',
      'git commit -m New-changes',
      'git push origin master'
      ]
    execute_commands(sentences)


