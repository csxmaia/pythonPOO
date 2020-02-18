def read():
  file_r = open("data.txt", "r")
  content = file_r.read()
  file_r.close()
  return content

def save(data):
  file_w = open("data.txt", "w")
  file_w.writelines("{}".format(data))
  file_w.close()