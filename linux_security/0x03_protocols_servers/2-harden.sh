#!/bin/bash
find / -type d -perm -0002 -xdev  -path -exec chmod o-w {} + 
