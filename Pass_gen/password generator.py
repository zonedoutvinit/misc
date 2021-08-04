import string
import random

if __name__ == "__main__":
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    plen = int(input("Enter password length: "))
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    f = open("C:/Users/Vinit/File/projects/Password gen/passwords.txt" , "a")
    print("Your password: ", end="" ,file = f)
    print("".join(random.sample(s, plen)) , file = f)
    f.close()
