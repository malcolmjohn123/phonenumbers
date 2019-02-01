import phonenumbers, xlrd
from phonenumbers import geocoder, carrier

def error_handling_func(phone_num):
	if (phonenumbers.is_valid_number(phone_num) == True) and (phonenumbers.is_possible_number(phone_num) == True):
		return 1
	else:
		return 0

def single_phonenumber(phone_num):
	if phone_num[0] == '+':
		phone_num = phonenumbers.parse(phone_num, None)
	elif phone_num[0] == '0':
		phone_num = phonenumbers.parse(phone_num, 'NP')
	return phone_num

def info_db(phone_num):
        phone_num = phonenumbers.format_number(phone_num, phonenumbers.PhoneNumberFormat.NATIONAL)
        file_location = "C:\\Users\\malcolmjohn\\Desktop\\advanced python\\Projects\\phone number\\landline.xlsx"
        workbook = xlrd.open_workbook(file_location)
        sheet = workbook.sheet_by_index(0)
        for i in range(sheet.nrows):
                if phone_num[1:3] == sheet.cell_value(i,1):
                        district = sheet.cell_value(i,0)
                        break
        return district

def display_phonenumber(phone_num, district):
    print phone_num
    print "Country:{}, District:{}".format(repr(geocoder.description_for_number(phone_num, 'en')), district)
    print "Network used:{}".format(repr(carrier.name_for_number(phone_num, 'en')))

def main():
        phone_num = raw_input("Enter your phonenumber:")
        phone_num = single_phonenumber(phone_num)
        error_value = error_handling_func(phone_num)
        if error_value == 1:
                district = info_db(phone_num)
                display_phonenumber(phone_num, district)
        else:
                print "Phone_number is not valid"

if __name__ == '__main__':
	main()







