numbers_holes = {
  4: 1,
  6: 1,
  8: 2,
  9: 1,
  0: 1
}

while True:
  user_input = None

  try:
    user_input = input('Hello, enter any numbers from 0 to 9 and I will tell you how many holes there are: ')

    user_input = [int(num) for num in user_input]

    if user_input[0] == 0: user_input.pop(0)

    holes = 0

    for num in user_input:
      if num in numbers_holes.keys():
        holes += numbers_holes[num]

    print(holes)
  except ValueError:
    print("error")