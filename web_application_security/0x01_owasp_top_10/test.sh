#!/bin/bash
for i in {0..20}; do
  curl "http://web0x01.hbtn/a1/hijack_session" | grep -i "hijack session"
done

