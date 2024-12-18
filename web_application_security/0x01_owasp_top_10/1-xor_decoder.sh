#!/bin/bash

hash=$1

hash=${hash#'{xor}'}

decoded_pass=$(echo "$hash" | base64 -d)

decodedp_xor=""
for ((i = 0; i < ${#decoded_pass}; i++)); do
    char="${decoded_pass:$i:1}"
    ascii_value=$(printf "%d" "'$char")
    xor_result=$((ascii_value ^ 95))
    decodedp_xor+=$(printf '\\x%x' $xor_result)
done

echo -e "$decodedp_xor"
