#!/bin/bash

# This script requires root or sudo privileges to show login info

# Check if the script is run with root privileges
if [ "$(id -u)" -ne 0 ]; then
  echo "This script must be run as root or with sudo."
  exit 1
fi

# Show the last 5 login sessions with user names and their corresponding dates
last -n 5
