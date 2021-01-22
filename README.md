# PythonExercise


``` python
def recursive(i):
    if i <= 10:
       i += 1
       print('hello ' + str(i))
       recursive(i)
    return

def main():
    i = 0
    print('Hello')
    recursive(i)

main()    
```
