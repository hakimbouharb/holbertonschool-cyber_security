#!/bin/bash
sudo ss -tpan | grep -E 'LISTEN|ESTAB'

