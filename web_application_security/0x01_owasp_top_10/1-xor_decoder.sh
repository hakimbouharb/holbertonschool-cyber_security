#!/bin/bash

password="$1"
password="${password#'{xor}'}"
decoded_password=$(echo "$password" | base64 -d)

decoded_password_xor=""
for ((i = 0; i < ${#decoded_password}; i++)); do
    char="${decoded_password:$i:1}"
    ascii_value=$(printf "%d" "'$char")
    xor_result=$(( ascii_value ^ 95 ))
    decoded_password_xor+="$(printf "$(printf '\\x%x' $xor_result)")"
done
echo "$decoded_password_xor"
