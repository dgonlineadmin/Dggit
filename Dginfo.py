dginfo=["tel":"01732227709","email":"dgonline24@gmail.com","mobile":"09217153808","address":"iran,golestan,gorgan,shohada street,laleh 5,7"]
while 1:
  s=input("enter word:").lower()
  if s in dginfo:
    print(f"{s}:",dginfo[s])
  else:
    print("not fount")
  if s=="exit":break
  
