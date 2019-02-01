import phonenumbers, xlrd
from phonenumbers import geocoder, carrier
from Tkinter import *
import tkMessageBox

def error_handling_func(phone_num):
    try:#handling given number can be parsed or not
        if phone_num[0] == '+':
            phone_num = phonenumbers.parse(phone_num, None)
        elif phone_num[0] == '0':
            phone_num = phonenumbers.parse(phone_num, 'NP')
    except AttributeError:
        tkMessageBox.showinfo("Number not entered properly", "Enter the number as shown")
    else:#if parsed also then checking is valid or not
        if (phonenumbers.is_valid_number(phone_num) == True) and (phonenumbers.is_possible_number(phone_num) == True):
            return phone_num
        else:
            tkMessageBox.showinfo("Wrong Number", "The phone number is not valid")

def info_db():#function for giving detail info
        phone_num = a.get()
        phone_num = error_handling_func(phone_num)
        if phone_num != None:
            text1.insert(0,str(geocoder.description_for_number(phone_num, 'en')))
            text2.insert(0,str(carrier.name_for_number(phone_num, 'en')))
            phone_num = phonenumbers.format_number(phone_num, phonenumbers.PhoneNumberFormat.NATIONAL)#if number given in international format then gets converted into nationalformat
            file_location = "C:\\Users\\malcolmjohn\\Desktop\\advanced python\\Projects\\phone number\\landline.xlsx"
            workbook = xlrd.open_workbook(file_location)#acessing excel file from location
            sheet = workbook.sheet_by_index(0)
            for i in range(sheet.nrows):
                    if phone_num[1:3] == sheet.cell_value(i,1):
                            district = sheet.cell_value(i,0)
                            break
            text3.insert(0,district)

def info_clear():#function for clearing out the info 
    text.delete(0,END)
    text1.delete(0, END)
    text2.delete(0, END)
    text3.delete(0, END)

#Creating customized window
myGui = Tk()
myGui.title("Phone_Info 2016 developed by MJT") 
myGui.geometry("800x800+500+100")

#creating labels for information
a = StringVar()
myLabel1 = Label(text="Get your phone info now...", fg="black", font=('arial',25,'bold')).pack()
blank_space = Label(text=" ", font=25).pack()
myLabel2 = Label(text="Number pattern(New dialing format from 14.III.2003)", font=('arial',15,'underline')).pack()
myLabel3 = Label(text="+977ABYXXXXX or 0ABYXXXXX", fg="black", bg="white" , font =('arial',15,'italic')).pack()
blank_space = Label(text=" ", font=25).pack()
blank_space = Label(text=" ", font=25).pack()
myLabel4 = Label(text="Enter your number below", fg="black", font=("arial",15)).pack()

#Creating text and button
text = Entry(myGui,textvariable=a, font=('arial',25))
text.pack()
myButton1 = Button(myGui,text="find_info", fg="black",font=("arial",15), command=info_db).pack()

#Label for outputs
blank_space = Label(myGui, text=" ", font=15).pack()
Label1 = Label(myGui, text = "Phone-Info", font=("arial",20,"bold")).pack()
Label2 = Label(myGui, text = "Country:", font=("arial",15,"italic")).pack()
text1 = Entry(myGui, width=25, font=("arial",15,))
text1.pack()
Label3 = Label(myGui, text = "NetworkUsed:", font=("arial",15,"italic")).pack() 
text2 = Entry(myGui, width=25, font=("arial",15,))
text2.pack()
Label4 = Label(myGui, text = "District:", font=("arial",15,"italic")).pack()
text3 = Entry(myGui, width=25, font=("arial",15,))
text3.pack()

#Button for clearing out
myButton2 = Button(myGui,text="clear", fg="black",font=("arial",15), command=info_clear).pack()

myGui.mainloop()





