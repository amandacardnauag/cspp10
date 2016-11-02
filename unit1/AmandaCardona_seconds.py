seconds = input(" Enter a number of seconds:")
seconds = int(seconds)
minutes = int(seconds / 60)
hours = int(minutes / 60)
s = seconds % 60
str(seconds)
str(minutes)
str(hours)
str(s)
print ( str(seconds) + " is " + str(hours) + " hours , " + str(minutes) + " minutes and " + str(s) + " seconds" )

