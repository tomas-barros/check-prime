from tkinter import *
from checkprime import check_prime

# variables
root = Tk()
labelvar = StringVar()

# config
root.title('Check primes')
labelvar.set('Generate a number first!')

# labels
label = Label(root, textvariable=labelvar)
label.pack()

# input
inpNumber = Entry(root, text='insert number here...')
inpNumber.pack()

# functions
def check_nmb():
    number = int(inpNumber.get())
    if check_prime(number):
        labelvar.set(f'{number} es primo')
    else:
        labelvar.set(f'{number} no es primo')

    print(check_prime(number))

# button
genNumberBtn = Button(root, command=check_nmb, text='Check')
genNumberBtn.pack()

# looping
root.mainloop()