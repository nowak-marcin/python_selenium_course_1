# np TypeError, DivisionByZeroError, IndexError, KeyError, NameError...
# jeśli w bloku try wystąpi exception, to wykonywany jest kod pod except
#
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
#   finally:
#       <do this whatever there is exception or not>
# --------------------------------------------
#   raise Exception('Test Failed')
# jeśli chcemy uznac exception za bład

try:
    a = 5 / 0
except ZeroDivisionError as e:
    print(f'wystapił blad: {e}')
    print('nie dziel przez zero !')

print('---------')

try:
    a = 5 / 0
except Exception as e:
    print(f'wystapił blad: {e}')

print('---------')

try:
    a = 5 / 'abc'
    b = 5 / 0
except Exception as e:
    print(f'wystapił blad: {e}')
    raise Exception('cos poszło nie tak...')

print('---------')

try:
    a = 5 / 'abc'
    b = 5 / 0
except (ZeroDivisionError, TypeError):
    print(f'wystapił blad')

print('---------')

try:
    a = 5 / 'abc'  # ten blad wystapi jako pierwszy
    b = 5 / 0
except ZeroDivisionError:
    print('nie dziel przez 0 !')
except TypeError:
    print('nie mieszaj typu str z typem int !')
    