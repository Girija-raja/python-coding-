import smtplib
from email.mime.text import MIMEText

sender_email = "girijarajamani2008@gmail.com"
receiver_email = "girijarajamani2008@gmail.com"
password = "crlc mknm rqjc gebq"

message = MIMEText("Hello! This is a test email sent using Python SMTP.")
message["Subject"] = "Python SMTP Test"
message["From"] = sender_email
message["To"] = receiver_email

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()  

    server.login(sender_email, password)

    server.send_message(message)

    print("Email sent successfully!")

except Exception as e:
    print("Error:", e)

finally:
    server.quit()
