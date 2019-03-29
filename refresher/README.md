# refresher -

```
files: refresh.py and refre.sh
```
` a shortcut for reverting a python virtualenv environment to a default/blank state (makes python3 instance by default*). `

` quickly tears down an active virtualenv instance and puts back up a fresh one in the same file location + `
` with the same name as the original instance! ^_^ `

### usage:
- while in the directory that holds the **active virtualenv's folder**, `python3 ~/.scripts/refresh.py` to revert to a fresh virtualenv instance

- add an alias for the script in bashrc: `alias refresh="python3 ~/.scripts/refresh.py"` (optional, obviously)

- `refresh.py` and `refre.sh` only need to be kept in the same folder as each other in order to call script from anywhere 
- having activated `virtualenv path/to/here/env1` by running `source env1/bin/activate`, running `refresh` in `path/to/here` will function like so:
<table><tr>
<td>
<img src="https://i.ibb.co/qD8Mj2H/refresh.png" width="100%">
</td></tr>
<tr><td><br>
· <b>pip freeze</b> shows us what the currently-active virtualenv <b>env1</b> has installed. 
(to demonstrate, <a href="https://pandas.pydata.org/"><b>pandas</b></a> module + dependencies were pre-installed.)<br><br>
· run <b>refresh</b>  to restore environment to new (verify with <b>freeze</b>.)<br><br>
· <b>pandas</b> and its dependencies are no longer installed - <b>env1</b> was refreshed.<br>
<br>
</td></tr></table>

---

**\*note:**  this script creates a **python3** virtualenv instance by default.

to specify another version, modify `refre.sh`, line 13: `virtualenv "$1" -p python3 --quiet` to `-p <version>`.
  
a future update will include a default python version you can set + optional version command line argument to specify a version to use this time.

---

`♡ thanks for checking it out ♡`
