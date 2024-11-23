#!/bin/bash
subfinder -d $1 -silent | xargs -I {} dig +short {} | paste -d, <(subfinder -d $1 -silent) - > "$1.txt"
