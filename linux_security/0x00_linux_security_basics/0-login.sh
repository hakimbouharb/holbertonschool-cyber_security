#!/bin/bash
if [[ $(id -u) -ne 0 ]]; then
last -n 5
echo "wtmp begins $(last -F | grep -m 1 -o '^[a-zA-Z0-9]\+')"
