print("let's see how long you've lived in days, minutes and seconds!")
print("ensure name does not contain numerics")
name = input("Name:")
print("Now enter your age:")
age = int(input("age:"))
days = age * 365
minutes = age * 525948
seconds = age * 31556926
print(name, "has been alive for", days, "days", minutes, "minutes,and" ,seconds, "seconds! Wow!")
