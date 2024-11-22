#!/bin/bash
[ $EUID -ne 0 ] && echo "Run as root or sudoer." && exit 1; sudo last -F -n 5
