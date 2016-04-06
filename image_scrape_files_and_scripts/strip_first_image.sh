#!/bin/sh

wget -O $1.jpg http:`egrep -v 'Wiktionary-logo-en.svg.png|Disambig_gray|CentralAutoLogin|wikimedia-button.png|poweredby_mediawiki|20px-Cscr-featured.svg.png' $1 |
grep img \
| head -n 1 | sed -e 's@.*src="\(.*\)"@\1@'  | awk '{print $1;}' | sed -e 's@"$@@'`

