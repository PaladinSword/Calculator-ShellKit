# Only integer calculation

a = "exit"
print("""
   ____        __                                 
  / __ \____  / /_  __                            
 / / / / __ \/ / / / /                            
/ /_/ / / / / / /_/ /                             
\____/_/ /_/_/\__, /                              
    ____     /____/                               
   /  _/___  / /____  ____ ____  _____            
   / // __ \/ __/ _ \/ __ `/ _ \/ ___/            
 _/ // / / / /_/  __/ /_/ /  __/ /                
/___/_/_/_/\__/\___/\__, /\___/_/   __            
  / ____/___ _/ /__/____/__/ /___ _/ /_____  _____
 / /   / __ `/ / ___/ / / / / __ `/ __/ __ \/ ___/
/ /___/ /_/ / / /__/ /_/ / / /_/ / /_/ /_/ / /    
\____/\__,_/_/\___/\__,_/_/\__,_/\__/\____/_/     """)
print("|--------------------------------------------------------------|")
print("|Announcement To log out, please type 'exit' instead of symbol!|")
print("|--------------------------------------------------------------|")

while True:
	one = (int(input("please enter a number: ")))
	two = (int(input("please enter a number: ")))
	symbol = (input("please enter a calculation symbol: "))
	if symbol == "+":
		print(one+two)
		continue
	if symbol == "-":
		print(one-two)
		continue
	if symbol == "/":
		print(one/two)
		continue
	if symbol == "*":
		print(one*two)
		continue
	if symbol == a:
		break
		pass
	else:
		print("try again 'etc: + - / *'")
		pass
		

				
