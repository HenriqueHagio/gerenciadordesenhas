#! python3
#pw.py - Um programa que armazena suas senhas NÃO é seguro, apenas para fins de estudo

PASSWORDS = {'email':'Mjfo#rIbv4N&',
	'blog':'W@E5DRKHoLuE',
	'senhadolol':'lPdR!SF!%Cpj',
	'Facebook':'U^PcW&SrzTKv'}

import sys, pyperclip
if len(sys.argv)<2:
   print('Usage: python pw.py[account]-copy account password')
   sys.exit()

account=sys.argv[1] #o primeiro argumento da linha de comando é o nome da conta

if account in PASSWORDS:
   pyperclip.copy(PASSWORDS[account])
   print('Password for ' + account + ' copied to clipboard.')
else:
   print('There is no account named' + account)	
