#to install prettytable package please use this command
#python -m pip install -U prettytable


from prettytable import PrettyTable
table=PrettyTable()
table.add_column("Poke'mon",["Pikachu","Squirtle","Charmender"])
table.add_column("Type",["Electric","Water","Fire"])
table.align="l"
print(table)