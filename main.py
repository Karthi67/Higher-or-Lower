def ran():
  global a,b,c
  import random 
  from game_data import data
  from art import logo,vs
  a=random.choice(data)
  print(f"{logo}A:{a['name']},{a['description']},{a['country']}")
  b=random.choice(data)
  c=random.choice(data)
  print(vs)
  print(f"{vs}B:{b['name']},{b['description']},{b['country']}")
  
def great():
  choose=input("Choose A or B ").lower()
  if choose=="a":
    if a["follower_count"] > b["follower_count"]:
      print("A is GREATEST")
      print("YOU WON")
      return 0
    else:
      print("LOST")
      return 1
  elif choose=="b":
      if a["follower_count"] < b["follower_count"]:
       print("B is GREATEST")
       print("yOU won")
       return 1
      else:
        print("lost")
        return 0
  elif a["follower_count"] == b["follower_count"]:
    print("EEqual")
def another():
  if 0:
    
    print(f"{logo}A:{a['name']},{a['description']},{a['country']}")
  
    print(f"{vs}C:{c['name']},{c['description']},{c['country']}")
    choose=input("Choose A or C ").lower()
    if choose=="c":
      if a["follower_count"] > c["follower_count"]:
          print("a is GREATEST")
          print("YOU lost")
      else:
          print("YOu WON")  
    elif choose=="a":
      if a["follower_count"] > c["follower_count"]:
          print("a is GREATEST")
          print("YOU won")
      else:
          print("YOu lost")  
  elif 1:
    print(f"B:{b['name']},{b['description']},{b['country']}")
    print(f"C:{c['name']},{c['description']},{c['country']}")
    choose=input("Choose B or C ").lower()
    if choose=="c" :
      if b["follower_count"] < c["follower_count"]:
        print("b is GREATEST")
        print("YOU lost")
      else :
        print("won")
    elif choose=="b":
      if b["follower_count"] > c["follower_count"]:
            print("b is GREATEST")
            print("YOU won")
      else:
           print("YOu lost")  
ran()
great()
another()
rep=input("Do u Continue").lower()
while rep=="yes":
  ran()
  great()
  another()
