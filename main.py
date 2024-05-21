import os
import csv
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Set app-specific password directly (for testing purposes)
os.environ['EMAIL_PASSWORD'] = 'qyaf kjjp sciv yhvz'

def send_email(receiver_email, Subject, body):
    sender_email = "shakibduste517@gmail.com" #Email id
    sender_password = os.getenv('Email_Password') #App specific password

    #setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['subject'] = Subject

    #add body to email
    message.attach(MIMEText(body, 'plain'))

    #create smtp session for sending the mail
    try:
        session = smtplib.SMTP_SSL('smtp.gmail.com', 465) #using gmail with the port
        #session.connect("smtp.gmail.com", 587)
        session.set_debuglevel(1)  # Enable debug output
        session.ehlo()  # Identify ourselves to the SMTP server
        #session.starttls #enable security
        session.ehlo()  # Re-identify ourselves as an encrypted connection
        session.login(sender_email,sender_password) # login with mail_id and app-specific password
        text = message.as_string() # to understand
        session.sendmail(sender_email, receiver_email, text)
        session.quit()
        print(f"Email sent to {receiver_email}")
    except smtplib.SMTPException as e:
        print(f"Error: unable to send email to {receiver_email}. Error: {str(e)}")

def check_birthdays():
    # Read birthdays from CSV file
    with open('birthdays.csv', newline='') as file:
        reader = csv.reader(file)
        next(reader) # Skip header row
        for row in reader:
            name = row[0]
            dob = row[1]
            receiver_email = row[2]
            dob_date = datetime.datetime.strptime(dob, "%d-%b-%Y").date()
            today = datetime.datetime.today()
            if today.month == dob_date.month and today.day == dob_date.day:
                subject = f"Happy Birthday, {name}"
                body = f"Dear {name},\n\nHappy Birthday! 🎉🎂\n\nBest wishes,\nShakib"
                send_email(receiver_email, subject, body)

# Call the function to check and send reminders
check_birthdays()
