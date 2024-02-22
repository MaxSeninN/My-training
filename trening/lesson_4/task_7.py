# def fact_0(n):
#     my_list = (fact_0((n - 1) * n) for n in range(n))
#     return my_list
#
# for el in fact_0(1):
#     print(el)
def fact(n):
    for i in range(1, n + 1):
        yield i
        if n == 0 or n == 1:
            return 1
        else:
            return i * fact(i - 1)

for el in fact(2):
    print(el)