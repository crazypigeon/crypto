class CaesarCrypt:
    def __init__(self):
        self.plain_alpha = 'abcdefghijklmnopqrstuvwxyz'
        self.crypt_alpha = ''  
        self.set_key()

    def set_key(self,shift=3):
        if 0 <= shift <= 25:
            self.shift = shift
            self.crypt_alpha = self.plain_alpha[shift:] + self.plain_alpha[:shift]
        else:
            raise ValueError("Shift must be between 0 and 25")

    def encrypt(self,plain_text):
        crypt_text = ''
        for l in plain_text:
            try:
                crypt_text += (self.crypt_alpha[self.plain_alpha.index(l)])
            except ValueError:
                pass
        return crypt_text