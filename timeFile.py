def parse (time):

  time.replace(" ", "")

  error = "You entered a time that does not exist"

  time = time.split(":")
  if len(time) != 2 or len(time[1]) != 4:
    return error
    

  hour = time[0]
  minutes = "".join([time[1][0],time[1][1]])
  ampm = "".join([time[1][2],time[1][3]])

  if (len(hour) != 2 and len(hour) != 1) or len(minutes) != 2 or len(ampm) != 2:
    return error

  try:
    hour = int(hour)
    minutes = int(minutes)
    ampm = str(ampm)
  except:
    return error

  if type(hour) is not int or type(minutes) is not int or type(ampm) is not str:
    return error

  if (hour > 12 or hour < 1) or (minutes > 59 or minutes < 0) or (ampm != 'am' and ampm != 'pm'):
    return error

  if hour == 12:
    hour = 0

  if ampm == "pm":
    hour += 12
    # if hour > 23:
    #   hour - 24
  
  hour = str(hour)
  minutes = str(minutes)

  if(hour == "0"):
    hour = "00"
  
  if(minutes == "0"):
    minutes = "00"
  
  if(len(minutes) == 1):
    minutes = "0" + minutes

  if(len(hour) == 1):
    hour = "0" + hour

  return str(hour) + ":" + str(minutes)

