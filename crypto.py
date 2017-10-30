import argparse

parser = argparse.ArgumentParser(description='Test')

parser.add_argument('-t',nargs='+',required=True,help='crypt some text',metavar='text to encrypt')
parser.add_argument('-s',choices=range(0,25),default=3,type=int,help='# of characters to shift')

from caesar import CaesarCrypt
crypt = CaesarCrypt()

crypt.set_key(parser.parse_args().s)

user_text = ' '.join(parser.parse_args().t)
print user_text
print crypt.encrypt(user_text)