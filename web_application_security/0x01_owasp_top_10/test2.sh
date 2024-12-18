#!/bin/bash
for i in {0..20}; do
  response=$(curl -s "http://web0x01.hbtn/a1/hijack_session")
  echo "$response" | grep -i "hijack session" && echo "Potential session hijack detected!"
  echo "$response" | grep -i "set-cookie"
done
