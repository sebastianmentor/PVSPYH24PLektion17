from typing import Optional, Iterable, Sequence, Callable, List, Dict


class MyClass:
    def __init__(self, arg1: str, arg2: int, arg3: list = None) -> None:
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3 if arg3 else []

    def print_arg3(self) -> None:
        for item in self.arg3:
            print(item)

    def get_arg2(self) -> int:
        return self.arg2

    def get_arg1(self) -> str:
        return self.arg1

    def __hash__(self):
        return hash(self.arg1)


def function_for_MyClass(my_class: MyClass) -> dict:
    return {my_class.arg1: len(my_class.arg1)}


def function2_for_MyClass(my_class: Optional[MyClass]) -> str:
    if my_class is None:
        return "Nothing"
    return my_class.get_arg1()


def function3_for_MyClass(seq: Sequence[MyClass]) -> None:
    for mc in seq:
        mc.print_arg3()


def function4_for_MyClass(itr: Iterable[MyClass]) -> None:
    if isinstance(itr, dict):
        for key, val in itr.items():
            print(key, val)

    function3_for_MyClass(itr)


mc1 = MyClass("Hello", 23)
mc2 = MyClass("Godbye", 12, ["Hejdå", "See ya", "Bon voyage"])
mc3 = MyClass("Beans", 1, [2, 3, 1])
mc4 = MyClass("", 300)

l_of_mc = [mc1, mc2, mc3, mc4]
t_of_mc = (mc1, mc2, mc3, mc4)
d_of_mc = {mc1: "First", mc2: "Second", mc3: "Third", mc4: "Fourth"}
s_of_mc = set(mc1, mc2, mc3, mc4)
