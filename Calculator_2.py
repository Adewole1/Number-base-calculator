from tkinter import *
from tkinter import messagebox
import string


class Root(Tk):
    
    def __init__(self):
        super().__init__()
        
        self.wm_title('Number Base Converter')
        self.geometry('505x240+500+200')
        self.separate = string.digits + string.ascii_uppercase
        self.precision = None
        
        menu = Menu(self)
        file_menu = Menu(menu, tearoff=0)
        
        file_menu.add_command(label='Instruction', command=self.instr)
        file_menu.add_separator()
        file_menu.add_command(label='About', command=self.about) 
        
        menu.add_command(label='Clear All', command=self.clear)
        menu.add_cascade(label='Help', menu = file_menu)
        menu.add_command(label='Exit', command=self.destroy)
        self.config(menu=menu)
        
        # self.label = Label(self, text='MEE 409 GROUP 3 NUMBER BASE CALCULATOR', fg='blue')
        # self.label.grid(row=0, column=0, columnspan=4)
              
        self.label1 = Label(self, text='Number: ')
        self.label1.grid(row=1,column=1)
                
        self.num_text = StringVar()
        self.num = Entry(self, textvariable=self.num_text)
        self.num.grid(row=1,column=2, pady=5)
                
        self.list1=Listbox(self,height=3,width=70)
        self.list1.grid(row=2,column=1, columnspan=3, padx=5, pady=5)
                
        binoct_btn = Button(self, text='Binary-Octal', width=17, relief=GROOVE, command = self.binoct)
        binoct_btn.grid(row=3, column=1, pady=2)
        
        bindec_btn = Button(self, text='Binary-Decimal', width=17, relief=GROOVE, command = self.bindec)
        bindec_btn.grid(row=3, column=2, pady=2)
        
        binhex_btn = Button(self, text='Binary-Hexadecimal', width=17, relief=GROOVE, command = self.binhex)
        binhex_btn.grid(row=3, column=3, pady=2)
        
        decbin_btn = Button(self, text='Decimal-Binary', width=17, relief=GROOVE, command = self.decbin)
        decbin_btn.grid(row=4, column=1, pady=2)
        
        decoct_btn = Button(self, text='Decimal-Octal', width=17, relief=GROOVE, command = self.decoct)
        decoct_btn.grid(row=4, column=2, pady=2)
        
        dechex_btn = Button(self, text='Decimal-Hexadecimal', width=17, relief=GROOVE, command = self.dechex)
        dechex_btn.grid(row=4, column=3, pady=2)
        
        octbin_btn = Button(self, text='Octal-Binary', width=17, relief=GROOVE, command = self.octbin)
        octbin_btn.grid(row=5, column=1, pady=2)
        
        octdec_btn = Button(self, text='Octal-Decimal', width=17, relief=GROOVE, command = self.octdec)
        octdec_btn.grid(row=5, column=2, pady=2)
        
        octhex_btn = Button(self, text='Octal-Hexadecimal', width=17, relief=GROOVE, command = self.octhex)
        octhex_btn.grid(row=5, column=3, pady=2)
        
        hexbin_btn = Button(self, text='Hexadecimal-Binary', width=17, relief=GROOVE, command = self.hexbin)
        hexbin_btn.grid(row=6, column=1, pady=2)
        
        hexdec_btn = Button(self, text='Hexadecimal-Octal', width=17, relief=GROOVE, command = self.hexoct)
        hexdec_btn.grid(row=6, column=2, pady=2)
        
        hexoct_btn = Button(self, text='Hexadecimal-Decimal', width=17, relief=GROOVE, command = self.hexdec)
        hexoct_btn.grid(row=6, column=3, pady=2)
                
        self.list1.insert(END, 'Enter the number you want to convert,\n')
        self.list1.insert(END, 'Use one of the buttons below to convert,\n')
        # self.list1.insert(END, 'Use UPPERCASE for hexadecimal letters.')
        
    def about(self):
        about = Help(self)
        about.grab_set()
        
    def instr(self):
        inst = Instruct(self)
        inst.grab_set()
        
    def clear(self):
        self.list1.delete(0, END)
        self.num.delete(0, END)
                
    
    def binoct(self):
        self.list1.delete(0, END)
        try:
            number = self.num_text.get()
            
            if '.' in number:
                integer_part, fractional_part = number.split('.')
                precision = len(fractional_part) 
                
                num_in_10 = int(integer_part, 2)
                sign = -1 if num_in_10 < 0 else 1
                num_in_10 *= sign
                ans0 = ''
                while num_in_10:
                    ans0 += self.separate[num_in_10 % 8]
                    num_in_10 //= 8
                if sign == -1:
                    ans0 += '-'
                integer_part = ans0[::-1]
                
                ans1 = 0
                for digit in range(1, len(fractional_part)):
                    ans1 += self.separate.index(fractional_part[digit-1]) *2**-digit
                answer = ans1
                ans2 = ''
                for i in range(precision):
                    tmp = answer * 8
                    itmp = int(tmp)
                    ans2 += str(self.separate[itmp])
                    answer = tmp - itmp
                fractional_part = ans2
                self.list1.insert(END, 'Answer is:\n')
                self.list1.insert(END, integer_part+'.'+fractional_part+' in base8')
            else:
                num_in_10 = int(number, 2)
                sign = -1 if num_in_10 < 0 else 1
                num_in_10 *= sign
                ans0 = ''
                while num_in_10:
                    ans0 += self.separate[num_in_10 % 8]
                    num_in_10 //= 8
                if sign == -1:
                    ans0 += '-'
                integer_part = ans0[::-1]
                self.list1.insert(END, 'Answer is:\n')
                self.list1.insert(END, integer_part+' in base8')
        except ValueError or TypeError:      # number was a str representing an int not a float
            self.list1.insert(END, 'Cannot convert number\n')
            self.list1.insert(END, 'Check the number and try again')
        self.num.delete(0, END)
        
        
    def bindec(self):
        self.list1.delete(0, END)
        try:
            number = self.num_text.get()
            
            if '.' in number:
                integer_part, fractional_part = number.split('.')
                precision = len(fractional_part)
                
                num_in_10 = int(integer_part, 2)
                sign = -1 if num_in_10 < 0 else 1
                num_in_10 *= sign
                ans0 = ''
                while num_in_10:
                    ans0 += self.separate[num_in_10 % 10]
                    num_in_10 //= 10
                if sign == -1:
                    ans0 += '-'
                integer_part = ans0[::-1]
                
                ans1 = 0
                for digit in range(1, len(fractional_part)):
                    ans1 += self.separate.index(fractional_part[digit-1]) *2**-digit
                answer = ans1
                ans2 = ''
                for i in range(precision):
                    tmp = answer * 10
                    itmp = int(tmp)
                    ans2 += str(self.separate[itmp])
                    answer = tmp - itmp
                fractional_part = ans2
                self.list1.insert(END, 'Answer is:\n')
                self.list1.insert(END, integer_part+'.'+fractional_part+' in base10')
            else:
                num_in_10 = int(number, 2)
                sign = -1 if num_in_10 < 0 else 1
                num_in_10 *= sign
                ans0 = ''
                while num_in_10:
                    ans0 += self.separate[num_in_10 % 10]
                    num_in_10 //= 10
                if sign == -1:
                    ans0 += '-'
                integer_part = ans0[::-1]
                self.list1.insert(END, 'Answer is:\n')
                self.list1.insert(END, integer_part+' in base10')
        except ValueError or TypeError:      # number was a str representing an int not a float
            self.list1.insert(END, 'Cannot convert number\n')
            self.list1.insert(END, 'Check the number and try again')
        self.num.delete(0, END)
        
        
    def binhex(self):
        self.list1.delete(0, END)
        try:
            number = self.num_text.get()
            
            if '.' in number:
                integer_part, fractional_part = number.split('.')
                precision = len(fractional_part)
                
                num_in_10 = int(integer_part, 2)
                sign = -1 if num_in_10 < 0 else 1
                num_in_10 *= sign
                ans0 = ''
                while num_in_10:
                    ans0 += self.separate[num_in_10 % 16]
                    num_in_10 //= 16
                if sign == -1:
                    ans0 += '-'
                integer_part = ans0[::-1]
                
                ans1 = 0
                for digit in range(1, len(fractional_part)):
                    ans1 += self.separate.index(fractional_part[digit-1]) *2**-digit
                answer = ans1
                ans2 = ''
                for i in range(precision):
                    tmp = answer * 16
                    itmp = int(tmp)
                    ans2 += str(self.separate[itmp])
                    answer = tmp - itmp
                fractional_part = ans2
            
                self.list1.insert(END, 'Answer is:\n')
                self.list1.insert(END, integer_part+'.'+fractional_part+' in base16')
            else:
                num_in_10 = int(number, 2)
                sign = -1 if num_in_10 < 0 else 1
                num_in_10 *= sign
                ans0 = ''
                while num_in_10:
                    ans0 += self.separate[num_in_10 % 16]
                    num_in_10 //= 16
                if sign == -1:
                    ans0 += '-'
                integer_part = ans0[::-1]
                self.list1.insert(END, 'Answer is:\n')
                self.list1.insert(END, integer_part+' in base16')
        except ValueError or TypeError:      # number was a str representing an int not a float
            self.list1.insert(END, 'Cannot convert number\n')
            self.list1.insert(END, 'Check the number and try again')
        self.num.delete(0, END)
        
        
    def octbin(self):
        self.list1.delete(0, END)
        try:
            number = self.num_text.get()
            
            if '.' in number:
                integer_part, fractional_part = number.split('.')
                precision = len(fractional_part)
                
                num_in_10 = int(integer_part, 8)
                sign = -1 if num_in_10 < 0 else 1
                num_in_10 *= sign
                ans0 = ''
                while num_in_10:
                    ans0 += self.separate[num_in_10 % 2]
                    num_in_10 //= 2
                if sign == -1:
                    ans0 += '-'
                integer_part = ans0[::-1]
                
                ans1 = 0
                for digit in range(1, len(fractional_part)):
                    ans1 += self.separate.index(fractional_part[digit-1]) *8**-digit
                answer = ans1
                ans2 = ''
                for i in range(precision):
                    tmp = answer * 2
                    itmp = int(tmp)
                    ans2 += str(self.separate[itmp])
                    answer = tmp - itmp
                fractional_part = ans2
                
                self.list1.insert(END, 'Answer is:\n')
                self.list1.insert(END, integer_part+'.'+fractional_part+' in base2')
            else:
                num_in_10 = int(number, 8)
                sign = -1 if num_in_10 < 0 else 1
                num_in_10 *= sign
                ans0 = ''
                while num_in_10:
                    ans0 += self.separate[num_in_10 % 2]
                    num_in_10 //= 2
                if sign == -1:
                    ans0 += '-'
                integer_part = ans0[::-1]
                self.list1.insert(END, 'Answer is:\n')
                self.list1.insert(END, integer_part+' in base2')
        except ValueError or TypeError:      # number was a str representing an int not a float
            self.list1.insert(END, 'Cannot convert number\n')
            self.list1.insert(END, 'Check the number and try again')
        self.num.delete(0, END)
        
            
    def octdec(self):
        self.list1.delete(0, END)
        try:
            number = self.num_text.get()
            
            if '.' in number:
                integer_part, fractional_part = number.split('.')
                precision = len(fractional_part)
                
                num_in_10 = int(integer_part, 8)
                sign = -1 if num_in_10 < 0 else 1
                num_in_10 *= sign
                ans0 = ''
                while num_in_10:
                    ans0 += self.separate[num_in_10 % 10]
                    num_in_10 //= 10
                if sign == -1:
                    ans0 += '-'
                integer_part = ans0[::-1]
                
                ans1 = 0
                for digit in range(1, len(fractional_part)):
                    ans1 += self.separate.index(fractional_part[digit-1]) *8**-digit
                answer = ans1
                ans2 = ''
                for i in range(precision):
                    tmp = answer * 10
                    itmp = int(tmp)
                    ans2 += str(self.separate[itmp])
                    answer = tmp - itmp
                fractional_part = ans2
                
                self.list1.insert(END, 'Answer is:\n')
                self.list1.insert(END, integer_part+'.'+fractional_part+' in base10')
            else:
                num_in_10 = int(number, 8)
                sign = -1 if num_in_10 < 0 else 1
                num_in_10 *= sign
                ans0 = ''
                while num_in_10:
                    ans0 += self.separate[num_in_10 % 10]
                    num_in_10 //= 10
                if sign == -1:
                    ans0 += '-'
                integer_part = ans0[::-1]
                self.list1.insert(END, 'Answer is:\n')
                self.list1.insert(END, integer_part+' in base10')
        except ValueError or TypeError:      # number was a str representing an int not a float
            self.list1.insert(END, 'Cannot convert number\n')
            self.list1.insert(END, 'Check the number and try again')
        self.num.delete(0, END)
        
          
    def octhex(self):
        self.list1.delete(0, END)
        try:
            number = self.num_text.get()
            
            if '.' in number:
                integer_part, fractional_part = number.split('.')
                precision = len(fractional_part)
                
                num_in_10 = int(integer_part, 8)
                sign = -1 if num_in_10 < 0 else 1
                num_in_10 *= sign
                ans0 = ''
                while num_in_10:
                    ans0 += self.separate[num_in_10 % 16]
                    num_in_10 //= 16
                if sign == -1:
                    ans0 += '-'
                integer_part = ans0[::-1]
                
                ans1 = 0
                for digit in range(1, len(fractional_part)):
                    ans1 += self.separate.index(fractional_part[digit-1]) *8**-digit
                answer = ans1
                ans2 = ''
                for i in range(precision):
                    tmp = answer * 16
                    itmp = int(tmp)
                    ans2 += str(self.separate[itmp])
                    answer = tmp - itmp
                fractional_part = ans2
                
                self.list1.insert(END, 'Answer is:\n')
                self.list1.insert(END, integer_part+'.'+fractional_part+' in base16')
            else:
                num_in_10 = int(number, 8)
                sign = -1 if num_in_10 < 0 else 1
                num_in_10 *= sign
                ans0 = ''
                while num_in_10:
                    ans0 += self.separate[num_in_10 % 16]
                    num_in_10 //= 16
                if sign == -1:
                    ans0 += '-'
                integer_part = ans0[::-1]
                self.list1.insert(END, 'Answer is:\n')
                self.list1.insert(END, integer_part+' in base16')
        except ValueError or TypeError:      # number was a str representing an int not a float
            self.list1.insert(END, 'Cannot convert number\n')
            self.list1.insert(END, 'Check the number and try again')
        self.num.delete(0, END)
        
        
    def decbin(self):
        self.list1.delete(0, END)
        try:
            number = self.num_text.get()
            
            if '.' in number:
                integer_part, fractional_part = number.split('.')
                precision = len(fractional_part)
                
                num_in_10 = int(integer_part, 10)
                sign = -1 if num_in_10 < 0 else 1
                num_in_10 *= sign
                ans0 = ''
                while num_in_10:
                    ans0 += self.separate[num_in_10 % 2]
                    num_in_10 //= 2
                if sign == -1:
                    ans0 += '-'
                integer_part = ans0[::-1]
                
                ans1 = 0
                for digit in range(1, len(fractional_part)):
                    ans1 += self.separate.index(fractional_part[digit-1]) *10**-digit
                answer = ans1
                ans2 = ''
                for i in range(precision):
                    tmp = answer * 2
                    itmp = int(tmp)
                    ans2 += str(self.separate[itmp])
                    answer = tmp - itmp
                fractional_part = ans2
                
                self.list1.insert(END, 'Answer is:\n')
                self.list1.insert(END, integer_part+'.'+fractional_part+' in base2')
            else:
                num_in_10 = int(number, 10)
                sign = -1 if num_in_10 < 0 else 1
                num_in_10 *= sign
                ans0 = ''
                while num_in_10:
                    ans0 += self.separate[num_in_10 % 2]
                    num_in_10 //= 2
                if sign == -1:
                    ans0 += '-'
                integer_part = ans0[::-1]
                self.list1.insert(END, 'Answer is:\n')
                self.list1.insert(END, integer_part+' in base2')
        except ValueError or TypeError:      # number was a str representing an int not a float
            self.list1.insert(END, 'Cannot convert number\n')
            self.list1.insert(END, 'Check the number and try again')
        self.num.delete(0, END)
        
        
    def decoct(self):
        self.list1.delete(0, END)
        try:
            number = self.num_text.get()
            
            if '.' in number:
                integer_part, fractional_part = number.split('.')
                precision = len(fractional_part)
                
                num_in_10 = int(integer_part, 10)
                sign = -1 if num_in_10 < 0 else 1
                num_in_10 *= sign
                ans0 = ''
                while num_in_10:
                    ans0 += self.separate[num_in_10 % 8]
                    num_in_10 //= 8
                if sign == -1:
                    ans0 += '-'
                integer_part = ans0[::-1]
                
                ans1 = 0
                for digit in range(1, len(fractional_part)):
                    ans1 += self.separate.index(fractional_part[digit-1]) *10**-digit
                answer = ans1
                ans2 = ''
                for i in range(precision):
                    tmp = answer * 8
                    itmp = int(tmp)
                    ans2 += str(self.separate[itmp])
                    answer = tmp - itmp
                fractional_part = ans2
                
                self.list1.insert(END, 'Answer is:\n')
                self.list1.insert(END, integer_part+'.'+fractional_part+' in base8')
            else:
                num_in_10 = int(number, 10)
                sign = -1 if num_in_10 < 0 else 1
                num_in_10 *= sign
                ans0 = ''
                while num_in_10:
                    ans0 += self.separate[num_in_10 % 8]
                    num_in_10 //= 8
                if sign == -1:
                    ans0 += '-'
                integer_part = ans0[::-1]
                self.list1.insert(END, 'Answer is:\n')
                self.list1.insert(END, integer_part+' in base8')
        except ValueError or TypeError:      # number was a str representing an int not a float
            self.list1.insert(END, 'Cannot convert number\n')
            self.list1.insert(END, 'Check the number and try again')
        self.num.delete(0, END)
        
        
    def dechex(self):
        self.list1.delete(0, END)
        try:
            number = self.num_text.get()
            
            if '.' in number:
                integer_part, fractional_part = number.split('.')
                precision = len(fractional_part)
                
                num_in_10 = int(integer_part, 10)
                sign = -1 if num_in_10 < 0 else 1
                num_in_10 *= sign
                ans0 = ''
                while num_in_10:
                    ans0 += self.separate[num_in_10 % 16]
                    num_in_10 //= 16
                if sign == -1:
                    ans0 += '-'
                integer_part = ans0[::-1]
                
                ans1 = 0
                for digit in range(1, len(fractional_part)):
                    ans1 += self.separate.index(fractional_part[digit-1]) *10**-digit
                answer = ans1
                ans2 = ''
                for i in range(precision):
                    tmp = answer * 16
                    itmp = int(tmp)
                    ans2 += str(self.separate[itmp])
                    answer = tmp - itmp
                fractional_part = ans2
                
                self.list1.insert(END, 'Answer is:\n')
                self.list1.insert(END, integer_part+'.'+fractional_part+' in base16')
            else:
                num_in_10 = int(number, 10)
                sign = -1 if num_in_10 < 0 else 1
                num_in_10 *= sign
                ans0 = ''
                while num_in_10:
                    ans0 += self.separate[num_in_10 % 16]
                    num_in_10 //= 16
                if sign == -1:
                    ans0 += '-'
                integer_part = ans0[::-1]
                self.list1.insert(END, 'Answer is:\n')
                self.list1.insert(END, integer_part+' in base16')
        except ValueError or TypeError:      # number was a str representing an int not a float
            self.list1.insert(END, 'Cannot convert number\n')
            self.list1.insert(END, 'Check the number and try again')
        self.num.delete(0, END)
        
        
    def hexbin(self):
        self.list1.delete(0, END)
        try:
            number = self.num_text.get()
            
            if '.' in number:
                integer_part, fractional_part = number.split('.')
                precision = len(fractional_part)
                
                num_in_10 = int(integer_part, 16)
                sign = -1 if num_in_10 < 0 else 1
                num_in_10 *= sign
                ans0 = ''
                while num_in_10:
                    ans0 += self.separate[num_in_10 % 2]
                    num_in_10 //= 2
                if sign == -1:
                    ans0 += '-'
                integer_part = ans0[::-1]
                
                ans1 = 0
                for digit in range(1, len(fractional_part)):
                    ans1 += self.separate.index(fractional_part[digit-1]) *16**-digit
                answer = ans1
                ans2 = ''
                for i in range(precision):
                    tmp = answer * 2
                    itmp = int(tmp)
                    ans2 += str(self.separate[itmp])
                    answer = tmp - itmp
                fractional_part = ans2
                
                self.list1.insert(END, 'Answer is:\n')
                self.list1.insert(END, integer_part+'.'+fractional_part+' in base2')
            else:
                num_in_10 = int(number, 16)
                sign = -1 if num_in_10 < 0 else 1
                num_in_10 *= sign
                ans0 = ''
                while num_in_10:
                    ans0 += self.separate[num_in_10 % 2]
                    num_in_10 //= 2
                if sign == -1:
                    ans0 += '-'
                integer_part = ans0[::-1]
                self.list1.insert(END, 'Answer is:\n')
                self.list1.insert(END, integer_part+' in base2')
        except ValueError or TypeError:      # number was a str representing an int not a float
            self.list1.insert(END, 'Cannot convert number\n')
            self.list1.insert(END, 'Check the number and try again')
        self.num.delete(0, END)
       
        
    def hexoct(self):
        self.list1.delete(0, END)
        try:
            number = self.num_text.get()
            
            if '.' in number:
                integer_part, fractional_part = number.split('.')
                precision = len(fractional_part)
                
                num_in_10 = int(integer_part, 16)
                sign = -1 if num_in_10 < 0 else 1
                num_in_10 *= sign
                ans0 = ''
                while num_in_10:
                    ans0 += self.separate[num_in_10 % 8]
                    num_in_10 //= 8
                if sign == -1:
                    ans0 += '-'
                integer_part = ans0[::-1]
                
                ans1 = 0
                for digit in range(1, len(fractional_part)):
                    ans1 += self.separate.index(fractional_part[digit-1]) *16**-digit
                answer = ans1
                ans2 = ''
                for i in range(precision):
                    tmp = answer * 8
                    itmp = int(tmp)
                    ans2 += str(self.separate[itmp])
                    answer = tmp - itmp
                fractional_part = ans2
                
                self.list1.insert(END, 'Answer is:\n')
                self.list1.insert(END, integer_part+'.'+fractional_part+' in base8')
            else:
                num_in_10 = int(number, 16)
                sign = -1 if num_in_10 < 0 else 1
                num_in_10 *= sign
                ans0 = ''
                while num_in_10:
                    ans0 += self.separate[num_in_10 % 8]
                    num_in_10 //= 8
                if sign == -1:
                    ans0 += '-'
                integer_part = ans0[::-1]
                self.list1.insert(END, 'Answer is:\n')
                self.list1.insert(END, integer_part+' in base8')
        except ValueError or TypeError:      # number was a str representing an int not a float
            self.list1.insert(END, 'Cannot convert number\n')
            self.list1.insert(END, 'Check the number and try again')
        self.num.delete(0, END)
        
        
    def hexdec(self):
        self.list1.delete(0, END)
        try:
            number = self.num_text.get()
            
            if '.' in number:
                integer_part, fractional_part = number.split('.')
                precision = len(fractional_part)
                
                num_in_10 = int(integer_part, 16)
                sign = -1 if num_in_10 < 0 else 1
                num_in_10 *= sign
                ans0 = ''
                while num_in_10:
                    ans0 += self.separate[num_in_10 % 10]
                    num_in_10 //= 10
                if sign == -1:
                    ans0 += '-'
                integer_part = ans0[::-1]
                
                ans1 = 0
                for digit in range(1, len(fractional_part)):
                    ans1 += self.separate.index(fractional_part[digit-1]) *16**-digit
                answer = ans1
                ans2 = ''
                for i in range(precision):
                    tmp = answer * 10
                    itmp = int(tmp)
                    ans2 += str(self.separate[itmp])
                    answer = tmp - itmp
                fractional_part = ans2
                
                self.list1.insert(END, 'Answer is:')
                self.list1.insert(END, integer_part+'.'+fractional_part+' in base10')
            else:
                num_in_10 = int(number, 16)
                sign = -1 if num_in_10 < 0 else 1
                num_in_10 *= sign
                ans0 = ''
                while num_in_10:
                    ans0 += self.separate[num_in_10 % 10]
                    num_in_10 //= 10
                if sign == -1:
                    ans0 += '-'
                integer_part = ans0[::-1]
                self.list1.insert(END, 'Answer is:')
                self.list1.insert(END, integer_part+' in base10')
        except ValueError or TypeError:      # number was a str representing an int not a float
            self.list1.insert(END, 'Cannot convert number')
            self.list1.insert(END, 'Check the number and try again')
        self.num.delete(0, END)
        
 
class Help(Toplevel):
    
    def __init__(self, parent):
        super().__init__(parent)
        self.wm_title("About")
        self.geometry('270x80')
        self.wm_maxsize(270,80)
        
        label = Label(self, text='This program converts number in different bases: \nHexadecimal, Decimal, Octal and Binary.\nThank you for using!')
        label.grid(row=0, column=0)
        
        ok = Button(self, text='OK', command=self.destroy, width=8, relief=FLAT)
        ok.grid(row=1, column=0)

class Instruct(Toplevel):
         
    def __init__(self,parent):
        super().__init__(parent)
        self.wm_title("Instruction")
        self.geometry('250x100')
        self.wm_maxsize(230,80)
        
        label = Label(self, text='Enter the number you want to convert,\nUse one of the buttons below to convert,\nUse UPPERCASE for hexadecimal letters.')
        label.grid(row=0, column=0)
        
        ok = Button(self, text='OK', command=self.destroy, width=8, relief=FLAT)
        ok.grid(row=1, column=0)
    
if __name__=='__main__':
    root=Root()
    root.maxsize(505,240)
    root.mainloop()
