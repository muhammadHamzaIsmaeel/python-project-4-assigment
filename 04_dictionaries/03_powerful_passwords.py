from hashlib import sha256

def hash_password(password):
    return sha256(password.encode()).hexdigest()

def login(email, stored_login, password_to_check):
    if email in stored_login and stored_login[email] == hash_password(password_to_check):
        return True
    return False

def main():
    stored_login = {
        "hamza@gmail.com": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",
        "code_in_placer@cip.org": "973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc",
        "student@stanford.edu": "882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb"
    }

    print(login("hamza@gmail.com", stored_login, "word"))  
    print(login("hamza@gmail.com", stored_login, "password")) 
    
    print(login("code_in_placer@cip.org", stored_login, "Karel")) 
    print(login("code_in_placer@cip.org", stored_login, "karel")) 
    
    print(login("student@stanford.edu", stored_login, "password"))  
    print(login("student@stanford.edu", stored_login, "123!456?789"))  

if __name__ == '__main__':
    main()    
