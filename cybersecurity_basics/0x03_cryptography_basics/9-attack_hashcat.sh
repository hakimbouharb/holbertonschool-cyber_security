#!/bin/bash
hashcat --stdout -a 1 wordlist1.txt wordlist2.txt > combined_wordlist.txt && hashcat -m 0 "$1" combined_wordlist.txt 
