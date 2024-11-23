#!/bin/bash
echo $(nslookup -type=TXT $1 | awk 'NR>2 {print $2}')
