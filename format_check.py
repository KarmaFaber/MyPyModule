import re 
from email_validator import validate_email, EmailNotValidError

#email format_cheker:
def check_email(email):
    try:
        v = validate_email(email)  # validate and get info
        email = v["email"]  # replace with normalized form
        return True
    except EmailNotValidError as e:
        # email is not valid, exception message is human-readable
        return str(e)

#-empty---------------------------
def empty_check(str):
    empty=""
    str = "    \n  \r  \t   "
    if not str.strip(): # The String Is Only Spaces!
        return empty==True

#-size-----------------------------
def size_check(str):
    return len(str)


#letters: lower and upper-----------
def cap_lov_up_check(str):
    str_up = 0
    str_lo = 0
    for i in str:
        if i.ispper():
            str_up += 1
        if i.islower():
            str_lo += 1
    #print("The number of uppercase letters in your phrase is:", str_up)
    #print("The number of lowercase letters in your phrase is:", str_lo)
    return str_lo, str_up

#numbers ----------------   
def num_check(str):
    str_num =0
    for i in str:
        if i.isnumeric():
            str_num += 1
    #print("The number of numbers in your phrase is:", str_num)
    return str_num
 
#-characters ----------------------
def char_check(str): 
    messOk="This Strign has special characters"
    messNotOk="This Strign has NOT special characters"
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]') 
     
    if(regex.search(str) == None): 
        return messNotOk 

    else: 
        return messOk 

