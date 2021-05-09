import random, string
from requests import Session
from colorama import Fore, init

init(convert=True)

print('%sSubsribe To Aaron And how many codes?%s ' % (Fore.RED, Fore.WHITE), end='')
amount = int(input())
for i in range(amount):
    code = "https://discordapp.com/gifts/%s" % (('').join(random.choices(string.ascii_letters + string.digits, k=16)))
    print('Code: %s' % (code))
    with open('codes.txt', 'a') as f:
        f.write('%s\n' % (code))
