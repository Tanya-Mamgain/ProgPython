# CHSINING OF .replace
letter = '''Dear <|Name|>,
             you are selected !!!
             <|Date|>'''
print(letter.replace("<|Name|>","Tanya").
        replace("<|Date|>","27 January 2025"))