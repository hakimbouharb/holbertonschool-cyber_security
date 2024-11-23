#!/bin/bash
nslookup -type=mx $1 | tail -n +3 | head -n 1 | awk '{print $2}'
