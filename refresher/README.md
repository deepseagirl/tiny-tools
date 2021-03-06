# refresher -

```
files: refresh.py and refre.sh
```
` a shortcut for reverting a python virtualenv environment to a default/blank state. `

` quickly tears down an active virtualenv instance and puts back up + activates a fresh one in the same file location + `
` with the same name as the original instance! ^_^ `

### usage:
- from any directory, `python3 path/to/refresh.py` to revert to a fresh virtualenv instance

- add an alias for the script in bashrc: `alias refresh="python3 path/to/refresh.py"` (optional, obviously)

- `refresh.py` and `refre.sh` only need to be kept in the same folder as each other in order to call script from anywhere 
- having activated virtualenv `env1` by running `source .../env1/bin/activate`, running `refresh` script will function like so:
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

**note:**  this script creates a **python3** virtualenv instance by default.

to specify another version, modify `refre.sh`, line 14: `-p python3` to `-p <desired version>`.
  
a future update will include a default which can be set + optional argument to provide version on the command line.

---

`♡ thanks for checking it out ♡`
