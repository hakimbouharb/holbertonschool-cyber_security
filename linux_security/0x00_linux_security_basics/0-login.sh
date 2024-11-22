#!/bin/bash
sudo last -n 5 -F | grep "$1"
