#!/bin/bash
[[ $EUID -ne 0 ]] && >&2; exit1; sudo last -n 5 | awk '{print $1,$5,$6,$7,$8,$9}'
