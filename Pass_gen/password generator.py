import string
import random

if __name__ == "__main__":
    s1 = string.ascii_lowercase  #creating 4 str var for different types of random string
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    plen = int(input("Enter password length: ")) #accepting Len for password
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    
    f = open("passwords.txt" , "a") #Saving the new string in .txt format
    print("Your password: ", end="" ,file = f)  #viewing the password string in console
    print("".join(random.sample(s, plen)) , file = f)
    f.close()
