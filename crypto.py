import argparse

parser = argparse.ArgumentParser(description='Test')

parser.add_argument('-t',nargs='+',required=True,help='crypt some text',metavar='text to encrypt')
parser.add_argument('-s',choices=range(0,25),default=3,type=int,help='# of characters to shift')

plain_alpha = 'abcdefghijklmnopqrstuvwxyz'
shift = parser.parse_args().s
crypt_alpha = plain_alpha[shift:] + plain_alpha[:shift]

plain_text = ' '.join(parser.parse_args().t)

print plain_alpha

print crypt_alpha


print plain_text

crypt_text = ''
for l in plain_text:
    try:
        crypt_text += (crypt_alpha[plain_alpha.index(l)])
    except ValueError:
        pass
print crypt_text