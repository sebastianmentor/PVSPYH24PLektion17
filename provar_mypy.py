from typing import List, Any, Sequence, Iterable, Union

class A:
    def __init__(self, a):
        self.a = a

    def print_my_a(self):
        print('Hej', (self.a))

def func(a:int, b:float) -> int:
    return int(a*b)

def func2(a:int, b:float) -> Sequence[int|str]:
    ret = []
    for one in range(int(a*b)):
        ret.append(1)

    # ret.append(str(len(ret)))

    return ret

def function_on_A(list_of_A:list[A], random_a:A) -> None:
    for a in list_of_A:
        if random_a.a == a:
            print("A is in the list")
        print(a.a)

d :dict[str,A] = {'first':A('5'), 'second':A(32)}

for key,val in d.items():
    print(key, val.a)

print(d['first'].print_my_a())

print(func(5, 2.12))
print(func2(3, 3.3))
print(f"{any([False, False, True])}")