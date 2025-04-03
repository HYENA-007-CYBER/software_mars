# MORSE CODE FOR EACH NUMBER AND ALPABET
MORSE_CODE_DICT = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3',
    '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8',
    '----.': '9'
}
#DEFINING FUNCTION
def decode_morse(morse_code):
    mc=morse_code.strip().split('/') #STORING THE MORSE CODE AS A LIST SEPERATED BY '/'
    dc=[] #CREATING A LIST FOR FINAL OUTPUT
    for i in mc:
        dw="" #CREATING A STRING TO APPEND EACH WORD IN FINAL LIST
        for j in i.split():
            dw += MORSE_CODE_DICT.get(j) #TO GET THE DECODED CHARACTER FROM DICTIONARY
        dc.append(dw) #APPENDING EACH WORD ON THE LIST        
    return ' '.join(dc) # returning the final decoded message

#FOR NOW GETTING INPUT MANUALLY
morse_code=input("ENTER THE MORSE CODE : ")
decoded_message = decode_morse(morse_code) # IMPLEMENTING FUNCTION 
print(decoded_message)


