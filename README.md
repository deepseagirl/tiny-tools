# tiny-tools
Just some lil quality of life improvement scripts, bash and python, nothing too earth-shattering going on here.

### 

### refresher
```
refresh your virtualenv to a default install with 1 command ~  
see refresher/README.md :)
```

### logparse.py
```
usage:
python logparse.py test.log
```

- produces a python list of each unique IP found in an apache log file, returned to function caller.
- list is also printed to console - just comment out lines 12 and 13 if you don't want this.


### wayback.sh
```
usage:
wayback-ff.sh oekakiBBS
```

- produces a browser window with [Wayback Machine](https://web.archive.org/) results for a query.
- the example would open this link in a new window: http://web.archive.org/*/oekakiBBS
- a quick bashrc alias simplifies even further: `alias wayback="~/.scripts/wayback-ff.sh"` -> `wayback oekakiBBS`
- includes a firefox-specific version and a generic version that relies on python to spawn instance of your default browser.


| version        | info           | etc  |
| :-------------: |:-------------:| :-----:|
| **wayback-ff**| firefox-specific | spawns private window |
| **wayback-py**      | uses default browser      |   requires python [(-m webbrowser)](https://docs.python.org/2/library/webbrowser.html) |
