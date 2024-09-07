print("""
    ____       _                     _   __                __                 ____                       
   / __ \_____(_)___ ___  ___       / | / /_  ______ ___  / /_  ___  _____   / __ \__  _____  _______  __
  / /_/ / ___/ / __ `__ \/ _ \     /  |/ / / / / __ `__ \/ __ \/ _ \/ ___/  / / / / / / / _ \/ ___/ / / /
 / ____/ /  / / / / / / /  __/    / /|  / /_/ / / / / / / /_/ /  __/ /     / /_/ / /_/ /  __/ /  / /_/ / 
/_/   /_/  /_/_/ /_/ /_/\___/    /_/ |_/\__,_/_/ /_/ /_/_.___/\___/_/      \___\_\__,_/\___/_/   \__, /  
                                                                                                /____/   
""")

print("|------------------------------------------------------------------|")
print("|if you want to exit the program, enter a negative number 'etc -1'!|")
print("|------------------------------------------------------------------|")

while True:
    number = int(input("please you want to query prime number enter a number: "))

    if number < 1:
        print("This number is not prime!")
        if number < 0:
            print("Exiting the program.")
            break
    else:
        for i in range(2, number):
            if number % i == 0:
                print("This number is not prime!")
                break
        else:
            print("This number is prime!")

