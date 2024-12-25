import re
Email = input("Enter Email: ")
if re.search(r'^([a-z]+[\._]?[a-z0-9]+([\\._][a-z0-9]+)?@[a-z]{2,}\.[a-z]{2,}(\.[a-z]{2,})?)$',Email) != None:
  #re.search('^([a-z]+[\\._]?[a-z0-9]+([\\._][a-z0-9]+)?@[a-z]{2,}\\.[a-z]{2,}(\\.[a-z]{2,})?)$',Email)
    print("Valid")
else:
    print("Invalid")
