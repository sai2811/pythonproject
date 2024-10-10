import pwinput


def login(username, password):
    correct_username = "python"
    correct_password = "java"
    
    return username == correct_username and password == correct_password


def main():
    max_attempts = 3
    
    for attempt in range(1,max_attempts + 1):
        input_username = input("ENTER USERNAME: ")
        input_password = pwinput.pwinput("ENTER PASSWORD: ")
        
        if login(input_username, input_password):
          print("Login successfull!")
          break
        if attempt != max_attempts:
          print(f"Try again. you have {max_attempts-attempt} attempt(s) left")
        else:
         print("Your account is Locked")
   
if __name__ == "__main__":
    main()
                
    
    




