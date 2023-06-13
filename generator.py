# Imports [External Libraries] 
import json
import string

# Main class
class generator():  
    ## Initialization of the object
    def __init__(self):
        self.encryption_key_file = "data/encryption_key.json"
        with open(self.encryption_key_file) as f: 
            self.data = json.load(f)
        
    ## Helping Functions
    def charType(self, character):
        value = None
        self.space = False
        if character in string.ascii_uppercase: 
            DictVal = 'capital'
        elif character in string.ascii_letters: 
            DictVal = 'small'
        elif character in string.digits: 
            DictVal = 'number' 
        else:
            DictVal = 'special'
        return str(DictVal) 
    
    def search_key_by_value(self, dictionary, value, type):
        for key, val in dictionary[type].items():
            if val == value:
                return key
        return None
    
    ## Main Encryption Function
    def encrypt(self, text):
        encrypted_text = ""
        for l in text: 
            DictVal = self.charType(l)
            encrypted_char = self.data[DictVal][l]
            encrypted_text = encrypted_text + encrypted_char
        self.encrypted_text = encrypted_text
        return str(encrypted_text)
    
    ## Main Decryption Function
    def decrypt(self, text):
        decrypted_text = ""
        for l in text: 
            DictVal = self.charType(l)
            decrypted_char = self.search_key_by_value(self.data, l, DictVal)
            decrypted_text = decrypted_text + decrypted_char
        return str(decrypted_text)        
