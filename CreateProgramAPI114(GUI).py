from currency_converter import CurrencyConverter
from datetime import date
from tkinter import *

#GUI_section
main_window = Tk()

#Welcome_Header_section
header_main_window = Label(main_window,text='Welcome',font=40).grid(row=0,column=0)
header2_main_window = Label(main_window,text='USD Currency Converter',font=40).grid(row=1,column=0)

#Main_field_GUI_section
input_us_dollar = Entry(main_window)
input_us_dollar.grid(row=2,column=0)
label_us_dollar = Label(main_window,text="US (Dollar)",font=20).grid(row=2,column=1)

#Convert_section
convert_button = Button(main_window,text="Convert",font=20,width=7,height=1)
convert_button.grid(row=3,column=0)

#Blueprint_result_convert
class result_convert_currency():
    text_currency = ''
    result_display = Entry(main_window)
    label_display = Label(main_window,text=text_currency,font=('Arial',15))

#Result_display_thb_section
class thb(result_convert_currency):
    text_currency = 'THB'

result_thb = thb()
result_thb.result_display.grid(row=4,column=0)
result_thb.label_display.grid(row=4,column=1)

main_window.mainloop()
