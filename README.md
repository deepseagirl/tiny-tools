# tiny-tools
Just some lil quality of life improvement scripts, nothing too earth-shattering going on here.

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
