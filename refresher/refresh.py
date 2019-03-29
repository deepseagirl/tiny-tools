import os
import subprocess
import sys

# shouldn't exist outside of a virtualenv
if hasattr(sys, 'real_prefix'):

	# refre.sh should be in the same folder as refresh.py!
	split_path = sys.path[0].splitlines() 
	script_path = split_path[0]
	script = ("%s/refre.sh" % script_path) # this is why!~

	venv_fullpath = sys.prefix # full path to virtualenv instance
	dirs = venv_fullpath.split("/") # virtualenv's python path
	venv_name = dirs[-1] # just the name of the virtualenv folder 
	delimiter = ("/%s" % venv_name)
	venv_parent = venv_fullpath.split(delimiter)[0] # for cd

	if os.path.isfile(script):
		print()
		subprocess.call(["bash", script, venv_name, venv_parent, venv_fullpath])

else:
	print("virtualenv not enabled.")
