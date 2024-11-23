#!/bin/bash
nslookup -type=A $1 | awk 'NR>2 {print $2}'
