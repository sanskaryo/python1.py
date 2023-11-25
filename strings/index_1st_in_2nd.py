main_string = "I love apples, apples are my favorite fruit"
sub_string = "apples"

indices = []
index = -1
while True:
  index = main_string.find(sub_string, index + 1)
  if index == -1:
    break
  indices.append(index)

print(indices)


