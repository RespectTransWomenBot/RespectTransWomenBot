import base64     
x = input("Enter the reddit password of your bot: ")
a = base64.b64encode(bytes(x, "utf-8"))
print("Encoded: " + str(a))
print("\nDecoded (to check): " + str(base64.b64decode(a).decode("utf-8", "ignore")))