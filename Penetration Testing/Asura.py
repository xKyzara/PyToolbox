#!/usr/bin/python3

# ---------------------------------------------
# ---				Asura					---
# ---------------------------------------------
#
# Archive password cracker using a brute-force dictionary attack, written by xKyzara (github.com/xKyzara) for Python 3
# Should work for either zip-files or 7z-files ...
#
# Example: ./Asura.py -f secret.zip -p password-list.txt

import sys
import getopt
import zipfile

def usage():
	print("Usage: python3 Asura.py -f /path/to/the/zipfile -p /path/to/the/dictionary")
	print("")
	print("Options:")
	print("-h --help			- print this usage information")
	print("-f --file			- specify the zipfile to bruteforce")
	print("-d --dictionary			- specify the dictionary wordlist to use while bruteforcing")
	print("")
	print("Example:")
	print("./Asura.py -f secret.zip -p password-list.txt")
	print("")

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def crack(file, pwlist):
	password = None
	pw_count = 0
	zipfile_object = zipfile.ZipFile(file)

	total_passwords = file_len(pwlist)
	print("Cracking Archive %s" %file, "with the password list %s" %pwlist, "containing %i possible passwords:" %total_passwords)

	with open(pwlist, 'r') as list:
		for line in list.readlines():
			password = line.strip('\n')
			try:
				zipfile_object.extractall(pwd=password)
				password = 'Password found: %s' % password
			except:
				pass
			pw_count = pw_count + 1
			sys.stdout.write("\rPasswords tested: %i" %pw_count)
			sys.stdout.write(" / %i" %total_passwords)
			sys.stdout.flush()
	list.close()


def main(argv):
	print("Archive Cracker \"Asura\" v0.1 written by xKyzara (github.com/xKyzara)")
	print("")

	if not len(sys.argv[1:]):
		usage()
		sys.exit()

	file = None
	pwlist = None

	# read the command line options
	try:
		opts, args = getopt.getopt(argv,"hf:p:",["file=","pwlist"])
	except getopt.GetoptError:
		print ("Error: Problem Getting the Command Line Arguments")
		sys.exit(2)
	for opt, arg in opts:
		if opt == "-h":
			usage()
			sys.exit()
		elif opt in ("-f", "--file"):
			file = arg
		elif opt in ("-p", "--pwlist"):
			pwlist = arg

	crack(file, pwlist)

if __name__ == "__main__":
	main(sys.argv[1:])