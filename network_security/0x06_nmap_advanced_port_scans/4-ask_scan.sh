#!/bin/bash
sudo nmap -sA -p $2 --open -v --reason --host-timeout 1000ms $1
