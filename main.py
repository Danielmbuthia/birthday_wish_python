##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import random
import pandas
import datetime as dt
import smtplib
from dotenv import dotenv_values

config = dotenv_values('.env')
MY_EMAIL = config['email']
MY_PASSWORD = config['password']

letter_1 = 'Letter_templates/letter_1.txt'
letter_2 = 'Letter_templates/letter_2.txt'
letter_3 = 'Letter_templates/letter_3.txt'

letter_list = [letter_1, letter_2, letter_3]
select_letter = random.choice(letter_list)

birthday_person = pandas.read_csv('birthdays.csv')

now = dt.datetime.now()
month = now.month
day = now.day

data_dict = {row.get('name'): row.get('email') for (index, row) in birthday_person.iterrows() if
             row.day == day and row.month == month}
if len(data_dict) > 0:
    for (name, email) in data_dict.items():
        with open(select_letter) as letter:
            letter_data = letter.readlines()
            list_word = ''
            for word in letter_data:
                string_replaced_name = (word.replace('[NAME]', name))
                list_word += string_replaced_name
            with smtplib.SMTP('smtp.gmail.com') as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL, to_addrs=email, msg=f'Subject:Happy Birthday\n\n{list_word}')
