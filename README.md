# PyToolbox
PyToolbox is a personal collection of python scripts for a variety of different tasks, mostly related to PenTesting or general IT-Security Stuff.



# Overview
Asura
A Python Cracker for Zip and 7z Archives using a Dictionary Bruteforce Attack.

Usage: 
  python3 asura.py -f /path/to/the/zipfile -p /path/to/the/dictionary"

Options:
  -h --help			      - print this usage information
  -f --file			      - specify the archive to bruteforce
  -d --dictionary			- specify the dictionary wordlist to use while bruteforcing

Examples:
  python3 asura.py -f <secret.zip> -p <password-list.txt>
