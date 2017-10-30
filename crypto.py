import argparse

alpha = 'abcdefghijklmnopqrstuvwxyz'
caesar = alpha[3:] + alpha[:3]

parser = argparse.ArgumentParser(description='Test')

parser.add_argument('-c',nargs='+',required=True,help='crypt some text',metavar='text to encrypt')

crypt_text = str(parser.parse_args().c)

print(crypt_text)