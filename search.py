import webbrowser

file_name = "photo_urls.txt"

file = open(file_name, "r")

num_lines = sum(1 for line in open(file_name))

for x in range(0, num_lines):

  this_url = file.readline()
  print (this_url)
  webbrowser.open(this_url, new=0)

 

