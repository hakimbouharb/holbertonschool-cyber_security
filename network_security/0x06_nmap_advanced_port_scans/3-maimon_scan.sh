#!/bin/bash
sudo nmap -sM -p http,https,ftp,ssh,telnet -vv --reason $1
