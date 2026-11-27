# You can't join a string with a number directly:

# python
# count = 5
# print("Total: " + count)        # ❌ TypeError
# print("Total: " + str(count))   # ✅ works
# print(f"Total: {count}")        # ✅ easiest way
# A method is a function attached to a value, used with a dot: text.method().

# Method	What it does	Example	Result
# .lower()	all lowercase	"PASSED".lower()	"passed"
# .upper()	all uppercase	"login".upper()	"LOGIN"
# .title()	first letter of each word capital	"valid user".title()	"Valid User"
# .capitalize()	only the first letter capital	"valid user".capitalize()	"Valid user"
# .strip()	removes spaces at start and end	" Login ".strip()	"Login"
# .replace(a, b)	replaces a with b	"login_test".replace("_", " ")	"login test"
# .startswith(x)	starts with x?	"TC_001".startswith("TC")	True
# .endswith(x)	ends with x?	"report.html".endswith(".html")	True
# .count(x)	how many times x appears	"banana".count("a")	3
# .find(x)	position of x (or -1 if not found)	"TC_001".find("_")	2

# Strings in Python are like a printed document: you can't edit the original paper. When you call .upper(), Python makes a photocopy in capital letters and hands it to you. The original paper stays the same.
# name=input("give me a module name: ")
# print(name.upper() , name.lower() , name.title() )
# store="TC_045"
# print(store[0])
# print(store[5])
# print(store[4:6])
# error_message= "Login failed: invalid password"
# print("invalid " in error_message)
# print("=" *30)

# raw_name =input("Please enter a raw test name: ")
# corrected_name = raw_name.strip()
# corrected_name = corrected_name.lower()
# corrected_name = corrected_name.capitalize()
# corrected_name = corrected_name.replace("_test","")
# corrected_name = corrected_name.replace("_"," ")
# is_login_test = "login" in corrected_name.lower()
# print(corrected_name)


raw_name = input("Please enter a raw test name: ")

corrected_name = raw_name.strip()
corrected_name = corrected_name.lower()
corrected_name = corrected_name.capitalize()
corrected_name = corrected_name.replace("_test", "")
corrected_name = corrected_name.replace("_", " ")

is_login_test = "login" in corrected_name.lower()

print("-" * 30)
print(f"Raw Name      : {raw_name}")
print(f"Clean Name    : {corrected_name}")
print(f"Length        : {len(corrected_name)} characters")
print(f"Is Login Test : {is_login_test}")
print("-" * 30)