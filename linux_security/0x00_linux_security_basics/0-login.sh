#!/bin/bash
[ $EUID -ne 0 ] && echo "Run as root or sudoer." && exit 1; last -n 5
