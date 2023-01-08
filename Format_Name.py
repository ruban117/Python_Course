def format_name(f_name,l_name):
  if f_name=="" or l_name=="":
    return "Hey please enter your name and also title!"
  new_f_name=f_name.title()
  new_l_name=l_name.title()
  return f"{new_f_name} {new_l_name}"

name=input("Enter your name: ")
title=input("Enter Your Title: ")
print(format_name(name,title))
 