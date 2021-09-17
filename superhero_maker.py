import time

def time_input(prompt, delay=0.5):
  answer = input(prompt)
  time.sleep(delay)
  return answer


print("Hello and welcome to icreate superhero?\n")

superhero_creator = time_input("Would you like to make a new superhero ")

if superhero_creator .strip() .lower() in ["yes", "ok", "yeah"]:
    print("Cool lets get started of creating your superhero..... ")

    gender = input("What gender do you prefer? ")
    superpower = input("What is your special superpower ")
    costume = input("What kind of clothes will your superhero will have to wear ")
    
    print("So the things I have recorded is that you want to be a " 
          + gender + " you wanted to have the superpower of " 
          + superpower + " you also wanted to wear a ")

else:
    print("Please then kindly get off our website ")
