#/usr/bin/env bash
prefix='http://web.archive.org/web/*/'
query="$prefix$1"
firefox -private $query