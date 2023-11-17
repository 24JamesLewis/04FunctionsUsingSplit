# print("What time is it?")
# time = input()

def meal_time(military_time):
  hours, minutes = military_time.split(":")
  hours = int(hours)
  minutes = int(minutes)

  if hours == 7 or hours == 8 and minutes == 0:
    return "Breakfast"
  elif hours == 12 or hours == 13 and minutes == 0:
    return "Lunch"
  elif hours == 18 or hours == 19 and minutes == 0:
    return "Dinner"
  else:
    return "Not time for any meals"



print("07:00 => ", meal_time("07:00"))
print("07:01 => ", meal_time("07:01"))
print("08:00 => ", meal_time("08:00"))
print("08:01 => ", meal_time("08:01"))
print("12:00 => ", meal_time("12:00"))
print("13:00 => ", meal_time("13:00"))
print("18:00 => ", meal_time("18:00"))
print("19:00 => ", meal_time("19:00"))
print("19:01 => ", meal_time("19:01"))
print("19:02 => ", meal_time("19:02"))

def get_filename_extension(filename):

  return filename.split(".")[-1]

print(get_filename_extension("hello.txt"))
print(get_filename_extension("hello.py"))
print(get_filename_extension("hello"))

def get_image_file(filename):
  if get_filename_extension(filename) == "jpg" or get_filename_extension(filename) == "jpeg" or get_filename_extension(filename) == "png" or get_filename_extension(filename) == "gif" or get_filename_extension(filename) == "tiff":
    return True
  else:
    return False
    
print(get_image_file("hello.jpg"))
print(get_image_file("hello.png"))
print(get_image_file("hello.bmp"))
print(get_image_file("hello.gif"))
print(get_image_file("hello.tiff"))
