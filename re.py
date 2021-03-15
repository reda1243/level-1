# Index = int(input('enter index '))
Value = input('replace the name ')
List = ['reda','fatiha','rim','yassine','rihanne']
if Value in List:
    List.remove(Value)
    print(List)
else:
    print(False)