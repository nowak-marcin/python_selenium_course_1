# można modyfikować
# zawiera różne typy danych
# dane mogą się powtarzać
# dane są indeksowane

pc = ['dell', 'hp', 'toshiba']

print(type(pc))
print(pc)
print(len(pc))

pc.append('apple')
pc.append('samsung')
print(pc)

a = pc.pop()
pc.remove('hp')
print(pc)
print(a)