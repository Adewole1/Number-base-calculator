import tkinter as tk
import string
from tkinter import messagebox

symbols = string.digits + string.ascii_uppercase

def from_base10(number, original_base):
    return int(number, original_base)

def to_other_base(number, new_base):
    sign = -1 if number < 0 else 1
    number *= sign
    ans = ''
    while number:
        ans += symbols[number % new_base]
        number //= new_base
    if sign == -1:
        ans += '-'
    return ans[::-1]

def fraction_from_base(number, original_base):
    ans = 0
    for i in range(1, len(number)+1):
        ans += symbols.index(number[i-1]) * original_base**-i
    return ans

def fraction_to_base(number, new_base, precision=None):
    ans = ''
    for i in range(precision):
        tmp = number * new_base
        itmp = int(tmp)
        ans += str(symbols[itmp])
        number = tmp - itmp
    return ans

def convert():
    listbox.delete(0, tk.END)
    try:
        number = num_text.get()
        f_base = int(from_base_text.get())
        t_base = int(to_base_text.get())
        if '.' in number:
            integer_part, fractional_part = number.split('.')
            precision = len(fractional_part)+1 #if precision is None else precision
            integer_part = to_other_base(
                from_base10(integer_part, f_base),
                t_base
            )
            fractional_part = fraction_to_base(
                fraction_from_base(fractional_part, f_base),
                t_base,
                precision
            )
            listbox.insert(tk.END, integer_part+'.'+fractional_part)
            listbox.insert(tk.END, 'in base' +str(t_base))
        
        else:
            listbox.insert(tk.END, to_other_base(from_base10(number, f_base), t_base)) 
            listbox.insert(tk.END, 'in base' +str(t_base))
        
    except ValueError or TypeError:
        messagebox.showerror("Error", 'The number cannot be converted \nTry again!')
    num1.delete(0, tk.END)
    num2.delete(0, tk.END)
    num3.delete(0, tk.END)

app = tk.Tk()

# message = 'Welcome to a number base calculator'
# messagebox.showinfo('Welcome', message)

app.wm_title('Number Base Conversion')
app.geometry('580x130+500+300')

label1 = tk.Label(app, text='Number: ')
label1.grid(row=1,column=1)
        
num_text = tk.StringVar()
num1 = tk.Entry(app, textvariable=num_text)
num1.grid(row=1,column=2)
        
label2 = tk.Label(app, text='From base: ')
label2.grid(row=2,column=1)
        
from_base_text = tk.StringVar()
num2 = tk.Entry(app, textvariable=from_base_text)
num2.grid(row=2,column=2)
        
label3 = tk.Label(app, text='To base: ')
label3.grid(row=3,column=1)
        
to_base_text = tk.StringVar()
num3 = tk.Entry(app, textvariable=to_base_text)
num3.grid(row=3,column=2)
        
listbox = tk.Listbox(app,height=2,width=80)
listbox.grid(row=0,column=1, columnspan=6, padx=5, pady=5)
        
convert_btn = tk.Button(app, text='Convert', width=17, command = convert)
convert_btn.grid(row=1, column=6)
        
listbox.insert(tk.END, 'Enter the number, the number base to convert from,')
listbox.insert(tk.END, 'the number base to convert to, and press convert button')
       
app.maxsize(580,130)
app.mainloop()