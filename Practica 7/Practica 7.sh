#!/bin/bash

ip address
curl ifconfig.me

nmap -sP --script vuln 10.0.2.15
nmap -sP --script default 192.168.1.68
nmap github.com

