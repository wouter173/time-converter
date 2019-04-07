import os
import deco
import timeFile as time

loop = False

debugTimes = (
  "12:00am",
  "12:01am",
  "1:00am",
  "11:00am",
  "11:59am",
  "12:00pm",
  "12:01pm",
  "1:00pm",
  "11:00pm",
  "11:59pm",
)

if os.uname()[0] == "Darwin":
  clear = "clear"
elif os.uname()[0] == "Linux":
  clear = "clear"
else:
  clear = "cls"
  
def main(commands = True):
  os.system("clear")
  print(deco.center("-=[ time converter ]=-", "-"))
  if commands == True:
    print(deco.green("type exit to exit the program"))
    print(deco.green("type debug to debug some basic times"))
    print("enter a time seperated by an ':' and end it with pm or am.")
    print("example: " + deco.green("09:45am"))

if __name__ == "__main__":
  main()
  loop = True

while loop == True:

  inp = input("> ")
  
  if inp == "exit":
    os.system(clear)
    print("goodbye!")
    exit()

  elif inp == "debug":
    os.system(clear)
    main(False)
    for x in debugTimes:
      space = ""
      if len(x) == 6:
        space = " "
      print(x + space + " -> " + deco.green(time.parse(x)))
    input("> ")
    main()


  else: 
    print(deco.green(time.parse(inp)))