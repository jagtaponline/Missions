# Check if the list has all integers or not
def check_int(list_of_int):
  for num in list_of_int:
    if not isinstance(num, int):
      return False
  return True

x = [1,23,34,233,4556,321,43,-3]
print(x, check_int(x))
x = [1,23,34,233,4556,321,43,3.5]
print(x, check_int(x))
