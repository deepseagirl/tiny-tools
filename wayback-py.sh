#/usr/bin/env bash
prefix='http://web.archive.org/web/*/'
query="$prefix$1"
python -m webbrowser $query