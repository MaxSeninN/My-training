from itertools import cycle, count

for el in count(3):
    if el > 10:
        break
    else:
        print(el)

end_inter = 0
my_list = [1, 2, 3]
for el in cycle(my_list):
    if end_inter > 10:
        break
    print(el)
    end_inter += 1

