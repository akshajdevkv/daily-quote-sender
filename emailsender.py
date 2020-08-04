import smtplib
import csv
import time
from string import Template
from email.message import EmailMessage


def send_emails(email_address,email_password):
    while True:
        with open('quotesource.txt','r') as f:
            quotes = f.read()
            daily_quote_num= 0
            for quote in quotes.splitlines():
                view_quote = quote
                # opening user database
                with open('database.csv', 'r') as csv_database:
                    database_reader = csv.reader(csv_database)
                    # looping through user database
                    
                    for database_info in database_reader:
                        user_name = database_info[0]
                        user_email = database_info[1]
                        # sending email
                        message = EmailMessage()
                        message['from'] = user_name
                        message['to'] = user_email
                        message['subject'] = 'Daily Quotes '+str(daily_quote_num)
                        t = Template('$quoteline\n \n Have a nice day $name !')
                        message.set_content(t.substitute(
                            quoteline= view_quote,name=user_name))
                        try:
                            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                                smtp.ehlo()
                                smtp.starttls()
                                smtp.login(email_address, email_password)
                                smtp.send_message(message)
                                smtp.quit()
                        except Exception as err:
                            print(err)
                        daily_quote_num += 1
                time.sleep(86400)

