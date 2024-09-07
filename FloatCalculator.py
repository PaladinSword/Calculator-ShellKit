# Only float calculation

print("""
   ____        __      ________            __  ______      __           __      __            
  / __ \____  / /_  __/ ____/ /___  ____ _/ /_/ ____/___ _/ /______  __/ /___ _/ /_____  _____
 / / / / __ \/ / / / / /_  / / __ \/ __ `/ __/ /   / __ `/ / ___/ / / / / __ `/ __/ __ \/ ___/
/ /_/ / / / / / /_/ / __/ / / /_/ / /_/ / /_/ /___/ /_/ / / /__/ /_/ / / /_/ / /_/ /_/ / /    
\____/_/ /_/_/\__, /_/   /_/\____/\__,_/\__/\____/\__,_/_/\___/\__,_/_/\__,_/\__/\____/_/     
             /____/                                                                           
""")

print("|--------------------------------------------------------------|")
print("|Announcement To log out, please type 'exit' instead of symbol!|")
print("|--------------------------------------------------------------|")

while True:
	one = (float(input("please enter a number: ")))
	two = (float(input("please enter a number: ")))
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
	if symbol == "exit":
		break
		pass
	else:
		print("try again 'etc: + - / *'")
		pass
