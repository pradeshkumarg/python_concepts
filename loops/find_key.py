key_location = "chair"

locations = ["garage", "living room", "chair", "closet"]

for i in locations:
    if key_location == i:
        print("Key is found in ",  i)
        break
    else:
        print("Key not found")