import webbrowser
import time

file_name = "photo_urls.txt"

file = open(file_name, "r")

num_lines = sum(1 for line in open(file_name))

googUrl = 'https://www.google.com/searchbyimage?&image_url='

pause = False

lower = 0

for x in range (lower,num_lines):
    
  for x in range(0, 4):
    this_url = file.readline()
    print (googUrl + this_url)
    webbrowser.open_new(googUrl + this_url)

  lower += 10  
      









  

  
  
   

