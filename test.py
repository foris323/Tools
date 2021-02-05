from aenum import Enum as Enum2, auto
from enum import Enum, EnumMeta, auto
from normalizing import NormalizedDict, normalize


x = NormalizedDict(ignore="_")


# x["A_C"] = 1
# x["ac"] = 2

# print(x)


# class Z(Enum2):
#     AAA_CCC = "SSS"

#     @classmethod
#     def _missing_name_(cls, name):
#         print("===========")
#         for member in cls:
#             if normalize(member.name.lower(), ignore="_") == normalize(name.lower(), ignore="_"):
#                 return member

# print(Z["AAA CCC"])


class CaseInsensitiveEnumMeta(EnumMeta):
    _data = {}

    def __getitem__(self, name):
        print(f"name: {name}")
        name_nor = normalize(name, ignore="_")
        print(f"name_nor: {name_nor}")
        print(self._data)
        if name_nor in self._data:
            return self._data[name_nor][1]
        print("GG")
        return super().__getitem__(name)

    def __setattr__(self, name, value):
        print(f"set {name} to {value}")
        name_nor = normalize(name, ignore="_")
        if name_nor in self._data:
            print(self)
            raise AttributeError('Cannot reassign members.')
        else:
            self._data[name_nor] = (name, value)
            return super().__setattr__(name_nor, value)

    def __getattr__(self, name):
        name_nor = normalize(name, ignore="_")
        if name_nor in self._data:
            return self._data[name_nor][1]
        else:
            self._data[name_nor] = (name)
            return super().__getattr__(name_nor)


# class Label(Enum, metaclass=CaseInsensitiveEnumMeta):
#     a = auto()
#     b = auto()

class Label(Enum, metaclass=CaseInsensitiveEnumMeta):
    a = auto()
    b = auto()


print(Label.__members__)
