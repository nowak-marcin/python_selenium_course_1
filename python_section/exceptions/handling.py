# np TypeError, DivisionByZeroError, IndexError, KeyError, NameError...
# jeśli w bloku try wystąpi exception, to wykonywany jest kod w except
# --------------------------------------------
#   try:
#       <do something>
#   except KeyError:
#       <do this if there is an exception/s>
# --------------------------------------------
#   try:
#       <do something>
#   except ValueError as e:
#       print(e)
#       <do this if there is an exception>
# --------------------------------------------
#   try:
#       <do something>
#   except:
#       <do this if there is an exception>
#   else:
#       <do this if there is not an exception>
#   finally:
#       <do this whatever there is exception or not>
# --------------------------------------------
# raise Exception('Test Failed') - jeśli chcemy uznac exception za bład


a = int(input('podaj liczbe: '))
b = int(input('podaj liczbe: ')) # podaj 0 dla wystąpienia wyjatku
c = 'abc'

try:
    w = a / b
    print(w)
except ZeroDivisionError as e:
    print(f'wystapił blad: {e}')
    print('nie dziel przez zero !')

print('=========')

try:
    w = a / b
    print(w)
except Exception as e:
    print(f'wystapił blad: {e}')
else:
    print('ta czesc wykona sie, jesli nie ma wyjatku')
finally:
    print('ta czesc wykona sie zawsze, nawet po wystapieniu wyjatku')

print('==========')

try:
    w = a / b
    z = w / c
    print(w, z)
except (ZeroDivisionError, TypeError):
    print(f'wystapił jeden z bledow')

print('---------')

try:
    w = a / c  # ten blad wystapi jako pierwszy
    z = w / b
    print(w, z)
except ZeroDivisionError:
    print('nie dziel przez 0 !')
except TypeError:
    print('nie mieszaj typu str z typem int !')

print('---------')

try:
    w = a / b
    z = b / b
    print(w, z)
except Exception as e:
    print(f'wystapił blad: {e}')
    raise Exception('cos poszło nie tak...')

print('---------')
