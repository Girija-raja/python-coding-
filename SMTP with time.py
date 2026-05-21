import smtplib
from email.message import EmailMessage
import time
from datetime import datetime


sender_email = "abc@gmail.com"
password = "ojoh abui bujh jhvy"

receiver_email = input("Enter receiver email: ")

print("Waiting to send mail at 14:22...")

while True:

    current_time = datetime.now().strftime("%H:%M")

    if current_time == "14:22":

        msg = EmailMessage()

        msg["Subject"] = "Python File Attachment"
        msg["From"] = sender_email
        msg["To"] = receiver_email

        msg.set_content(
            "Hello! This mail contains a text file attachment."
        )

        file_path = r"D:/girija/day 1/basics.txt"

        try:

            with open(file_path, "rb") as file:
                file_data = file.read()

            msg.add_attachment(
                file_data,
                maintype="text",
                subtype="plain",
                filename="basics.txt"
            )

            server = smtplib.SMTP(
                "smtp.gmail.com",
                587
            )

            server.starttls()

            server.login(
                sender_email,
                password
            )

            server.send_message(msg)

            print("Email sent automatically at", current_time)

            server.quit()

            break

        except Exception as e:
            print("Error:", e)
            break

    time.sleep(30)

 
