from tkinter import *
from tkinter import ttk
from forex_python.converter import CurrencyRates

currency_rates = CurrencyRates()

def convert(event):
    result_convert = currency_rates.convert(from_selected.get(),to_selected.get(),float(box_amount.get()))
    result.configure(text = "%.2f" % result_convert)


main_window = Tk()
main_window.title('Currency Converter')
main_window.geometry('400x200')
label = Label(main_window, text = 'Currency Converter', fg = 'steel blue', font = ('Sukhumvit Set', 14, 'bold'))
label.grid(row = 0, column = 1)

#amount
label_amount = Label(main_window,text ='Amount', font = ('Sukhumvit Set', 14))
label_amount.grid(row = 1, column = 0)
box_amount = Entry(main_window, font = ('Sukhumvit set', 14) )
box_amount.grid(row = 1, column = 1)

#from currency
label_from_currency = Label(main_window, text = 'From', font = ('Sukhumvit set', 14))
label_from_currency.grid(row=2, column = 0)
from_selected = ttk.Combobox(main_window, font = ('Sukhumvit set', 14) )
from_selected['values'] = list(currency_rates.get_rates("").keys())
from_selected.bind("<<ComboboxSelected>>")
from_selected.grid(row = 2, column = 1)
from_selected.current()



#to currency
label_to_currency = Label(main_window, text = 'To', font = ('Sukhumvit set', 14))
label_to_currency.grid(row=3, column = 0)
to_selected = ttk.Combobox(main_window,font = ('Sukhumvit set', 14) )
to_selected['values'] = list(currency_rates.get_rates("").keys())
to_selected.bind("<<ComboboxSelected>>")
to_selected.grid(row = 3, column = 1)
from_selected.current()

#Convert
covert_button = Button(main_window, text = 'Convert', font = ('Sukhumvit set', 14))
covert_button.grid(row = 5, column = 1)
covert_button.bind('<Button-1>',convert)

#Result
result = Label(main_window, text = 'Result', fg = 'Blue', font = ('Sukhumvit set', 14))
result.grid(row = 7, column = 1)

main_window.mainloop()
