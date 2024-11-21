#!/bin/bash
cat /dev/urandom | tr -dc '[:alum:]' | fold -w  $1| head -n 1
