#!/bin/bash
echo "$1 ALL=(ALL) NOPASSWD: $0" | sudo tee -a /etc/sudoers
