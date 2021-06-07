from openpyxl import load_workbook
import pandas as pd

###########################################################################


def vigenere_enc(value):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    input_string = ""
    enc_key = "camilonore"
    enc_string = ""

    # Takes string from user
    input_string = value
    input_string = input_string.lower()

    # Lengths of input_string
    string_length = len(input_string)

    # Expands the encryption key to make it longer than the inputted string
    expanded_key = enc_key
    expanded_key_length = len(expanded_key)

    while expanded_key_length < string_length:
        # Adds another repetition of the encryption key
        expanded_key = expanded_key + enc_key
        expanded_key_length = len(expanded_key)

    key_position = 0

    for letter in input_string:
        if letter in alphabet:
            # cycles through each letter to find it's numeric position in the alphabet
            position = alphabet.find(letter)
            # moves along key and finds the characters value
            key_character = expanded_key[key_position]
            key_character_position = alphabet.find(key_character)
            key_position = key_position + 1
            # changes the original of the input string character
            new_position = position + key_character_position
            if new_position > 26:
                new_position = new_position - 26
            new_character = alphabet[new_position]
            enc_string = enc_string + new_character
        else:
            enc_string = enc_string + letter
    return(enc_string)


def vigenere_dec(value, enckey):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    input_string = ""
    dec_key = ""
    dec_string = ""

    dec_key = str(enckey)
    # Takes string from user
    input_string = value
    input_string = input_string.lower()

    # Lengths of input_string
    string_length = len(input_string)

    # Expands the encryption key to make it longer than the inputted string
    expanded_key = dec_key
    expanded_key_length = len(expanded_key)

    while expanded_key_length < string_length:
        # Adds another repetition of the encryption key
        expanded_key = expanded_key + dec_key
        expanded_key_length = len(expanded_key)

    key_position = 0

    for letter in input_string:
        if letter in alphabet:
            # cycles through each letter to find it's numeric position in the alphabet
            position = alphabet.find(letter)
            # moves along key and finds the characters value
            key_character = expanded_key[key_position]
            key_character_position = alphabet.find(key_character)
            key_position = key_position + 1
            # changes the original of the input string character
            new_position = position - key_character_position
            if new_position > 26:
                new_position = new_position + 26
            new_character = alphabet[new_position]
            dec_string = dec_string + new_character
        else:
            dec_string = dec_string + letter
    return(dec_string)

###########################################################################


class Functions:
    def __init__(self, function, domain, email='None', password='None') -> None:
        self.function = function
        self.domain = domain
        self.email = email
        self.password = password
        self.wb = load_workbook('Python\Tkinter\Password.xlsx')
        self.ws = self.wb.active
        self.ws.tittle = 'Passwords'
        self.counter = self.ws['F1'].value
        if self.function == 'add':
            self.AddData()
        elif self.function == 'delete':
            self.DeleteData()
        elif self.function == 'change':
            self.ChangePass()

    def AddData(self):
        # Asign values
        self.ws['A'+str(self.counter)].value = self.domain
        self.ws['B'+str(self.counter)].value = vigenere_enc(self.email)
        self.ws['C'+str(self.counter)].value = vigenere_enc(self.password)
        # Increasing counter value
        self.counter += 1
        # Asign the new counter value
        self.ws['F1'].value = self.counter
        self.wb.save('Python\Tkinter\Password.xlsx')
        print('Data successfully added')

    def DeleteData(self):
        DomainPositioin = self.LookFor(self.domain, self.counter)
        self.ws.delete_rows(DomainPositioin)
        self.wb.save('Python\Tkinter\Password.xlsx')
        print('Data successfully deleted')

    def KnowPassword(self, enckey):
        PasswordPosition = 'C'+str(self.LookFor(self.domain, self.counter))
        PasswordValue = self.ws[PasswordPosition].value
        PasswordValue = vigenere_dec(PasswordValue, enckey)
        return PasswordValue

    def ChangePass(self, newpassword):
        PasswordPosition = 'C'+str(self.LookFor(self.domain, self.counter))
        self.ws[PasswordPosition] = vigenere_enc(newpassword)
        self.wb.save('Python\Tkinter\Password.xlsx')
        print('Password successfully changed')

    def LookFor(self, domain, counter):
        for i in range(0, counter):
            df = pd.read_excel(
                "Python\Tkinter\Password.xlsx", "Sheet")
            if df.iloc[i, 0] == domain:
                return (i+2)


if __name__ == '__main__':
    Functions
