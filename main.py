##################### Extra Hard Starting Project ######################
import pandas as p
import datetime as dt
import random
import smtplib

birthdays = p.DataFrame()
today = (dt.datetime.now().day, dt.datetime.now().month)
b_day_person = p.DataFrame()
p_mail = ''
p_password = ''

with open('birthdays.csv', 'r') as f:
    birthdays = p.read_csv(f)

b_day_dict = {(birthdays_row['day'], birthdays_row['month']): birthdays_row for (index, birthdays_row) in
             birthdays.iterrows()}
b_day_person = b_day_dict[today]
if today in b_day_dict:
    filepath = f'letter_templates/letter_{random.randint(1,3)}.txt'
    with open(filepath) as letter_file:
        contents = letter_file.read()
        contents = contents.replace('[NAME]', b_day_person['name'])

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=p_mail, password=p_password)
        connection.sendmail(from_addr=p_mail, to_addrs=b_day_person['email'],
                            msg=f'Subject:Happy birthday!\n\n{contents}')
        connection.close()
