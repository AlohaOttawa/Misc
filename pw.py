#! python3
# pw.py - An insecure password locker program

PASSWORDS = {'email': 'F7min1basfdwer23dfs', 
			 'blog': 'AVAST23423dgsdf',
			 'luggage': '21345'}

import sys, pyperclip

if len(sys.argv) < 2:
	print('Usage: python pw.py [account] - copy account password')
	sys.exit()

account = sys.argv[1]		# first command line arg is the account name

if account in PASSWORDS:
	pyperclip.copy(PASSWORDS[account])
	print('Password for ' + account + ' copied to clipboard.')
else:
	print('Password not found for ' + account)