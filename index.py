import os
import deco
import timeFile as time

loop = False
  
def main():
  os.system("clear")
  print(deco.center("-=[ time converter ]=-", "-"))
  print(deco.green("type exit to exit the program"))
  print("enter a time seperated by an ':' and end it with pm or am.")
  print("example: " + deco.green("09:45am"))

if __name__ == "__main__":
  main("time converter")
  loop = True

while loop == True:

  inp = input("> ")
  
  if inp == "exit":
    os.system("clear")
    print("goodbye!")
    exit()

  else: 
    print(deco.green(time.parse(inp)))