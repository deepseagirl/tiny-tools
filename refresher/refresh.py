import os
import subprocess
import sys

# shouldn't exist outside of a virtualenv
if hasattr(sys, 'real_prefix'):

	# refre.sh should be in the same folder as refresh.py!
	split_path = sys.path[0].splitlines() 
	script_path = split_path[0]
	script = ("%s/refre.sh" % script_path) # this is why!~
	
	dirs = sys.prefix.split("/") # virtualenv's python path
	venv_dir = dirs[-1] # just the name of the virtualenv folder 
	if os.path.isfile(script):
		subprocess.call(["bash", script, venv_dir])

else:
	print("virtualenv not enabled.")
