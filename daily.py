import subprocess
import os

def command_line(cmd):
    """Handle the command line call
    keyword arguments:
    cmd = a list
    return
    0 if error
    or a string for the command line output
    """
    try:
        s = subprocess.check_output(cmd)
        return s.strip()
    except subprocess.CalledProcessError:
        return 0

#Change to the current directory
def cd_to_this_file_directory():
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

cd_to_this_file_directory()

with open('README.md', 'a') as myfile:
    myfile.write(' .')

command_line(['git', 'add', '*'])
command_line(['git', 'commit', '-m', 'New changes'])
command_line(['git', 'push', 'origin', 'master'])


