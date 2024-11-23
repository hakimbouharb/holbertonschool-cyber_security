#!/bin/bash
nslookup $1 | grep 'Address' | awk '{print $2}'
