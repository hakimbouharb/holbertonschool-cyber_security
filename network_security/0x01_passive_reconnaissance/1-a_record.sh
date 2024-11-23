#!/bin/bash
echo $(nslookup $1 | grep 'Address' | awk '{print $2}')
