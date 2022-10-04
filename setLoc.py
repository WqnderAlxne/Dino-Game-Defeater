import time
import win32gui

time.sleep(1)
flags, hcursor, (x,y) = win32gui.GetCursorInfo()

txt = open("loc.txt", "r+")
txt.truncate(0)

txt.write(str(x) + "\n")
txt.write(str(y) + "\n")
txt.write(str(x) + "\n")
txt.write(str(int(y*0.834600760456)) + "\n")

print("Wrote", x,y, "to loc.txt")