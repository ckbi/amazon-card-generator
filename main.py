
import time
import random
print(""" __   ____  ____   ___         ____    ___  ____     ___  ____    ____  ______   ___   ____  
   /  ] /    ||    \ |   \       /    |  /  _]|    \   /  _]|    \  /    ||      | /   \ |    \ 
  /  / |  o  ||  D  )|    \     |   __| /  [_ |  _  | /  [_ |  D  )|  o  ||      ||     ||  D  )
 /  /  |     ||    / |  D  |    |  |  ||    _]|  |  ||    _]|    / |     ||_|  |_||  O  ||    / 
/   \_ |  _  ||    \ |     |    |  |_ ||   [_ |  |  ||   [_ |    \ |  _  |  |  |  |     ||    \ 
\     ||  |  ||  .  \|     |    |     ||     ||  |  ||     ||  .  \|  |  |  |  |  |     ||  .  \
 \____||__|__||__|\_||_____|    |___,_||_____||__|__||_____||__|\_||__|__|  |__|   \___/ |__|\_|
                                                                                                """)
def g(rolls):
	data = "qwertyuioplkjhgfdsazxcvbnm1234567890QWERTYUIOPLKJHGFDSAZXCVBNM"
	result = ""
	while rolls >= 1:
		c = random.choice(data)
		result = c + result
		rolls = rolls - 1
	return result

#interface
print("Multiple Gift Card Generator")
print("")
print("What Giftcard you need to generate?")

tt = input("\nAmazon\nRoblox\nWebkinz\nFortnite\nIMVU\nEbay\nNetflix\niTunes\nPaypal\nVisa\nPokemonTGC\nPlaystation\nSteam\nXbox\nPlayStore\nMinecraft\n\n>")

t = tt.lower()
print("")
print("How many of them?")
nn = input(">")
print("")
n = int(nn)

if t == "minecraft":
	for x in range(n):
		print("")
		print(g(4)+"-"+g(4)+"-"+g(4))
		
if t == "paypal":
	for x in range(n):
		print("")
		print(g(4)+"-"+g(4)+"-"+g(4))
		
if t == "playstation":
	for x in range(n):
		print("")
		print(g(4)+"-"+g(4)+"-"+g(4))
		
if t == "amazon":
	for x in range(n):
		print("")
		print(g(4)+"-"+g(6)+"-"+g(4))
		
if t == "netflix":
	for x in range(n):
		print("")
		print(g(4)+"-"+g(6)+"-"+g(4))
		
if t == "steam":
	for x in range(n):
		print("")
		print(g(4)+"-"+g(6)+"-"+g(5))
		
if t == "fortnite":
	for x in range(n):
		print("")
		print(g(5)+"-"+g(4)+"-"+g(4))
		
if t == "robolox":
	for x in range(n):
		print("")
		print(g(3)+"-"+g(3)+"-"+g(4))
		
if t == "itunes":
	for x in range(n):
		print("")
		print(g(16))
		
if t == "ebay":
	for x in range(n):
		print("")
		print(g(10))
		
if t == "imvu":
	for x in range(n):
		print("")
		print(g(10))
		
if t == "webkinz":
	for x in range(n):
		print("")
		print(g(8))
		
if t == "pokemontgc":
	for x in range(n):
		print("")
		print(g(3)+"-"+g(4)+"-"+g(3)+"-"+g(3))
		
if t == "playstore":
	for x in range(n):
		print("")
		print(g(4)+"-"+g(4)+"-"+g(4)+"-"+g(4)+"-"+g(4))
		
if t == "xbox":
	for x in range(n):
		print("")
		print(g(5)+"-"+g(5)+"-"+g(5)+"-"+g(5)+"-"+g(5))

print("")
print("-----Generation completed-----")
time.sleep(360)
