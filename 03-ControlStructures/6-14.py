facebook = input("Does your influencer have facebook account? ")
twitter = input("Does your influencer have twitter account? ")
instagram = input("Does your influencer have instagram account? ")
if facebook == "True" and twitter == "True" and instagram == "False":
    print(f"You are a good influencer!")
elif facebook == "True" and instagram == "True" and twitter == "False":
    print(f"You are a good influencer!")
elif twitter == "True" and instagram == "True" and facebook == "False":
    print(f"You are a good influencer!")
elif facebook == "True" and instagram == "True" and twitter == "True":
    print(f"You are a good influencer!")
else:
    print(f"You are a bad influencer")