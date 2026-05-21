import smtplib
from email.message import EmailMessage


sender_email = "abc@gmail.com"
password = "gnlb dsjh sjhm shjm"


receiver_email = input("Enter receiver email: ")


msg = EmailMessage()

msg["Subject"] = "Python File Attachment"
msg["From"] = sender_email
msg["To"] = receiver_email

msg.set_content("Hello! This mail contains a text file attachment.")


file_path = r"D:/bja/day 1/basics.txt"

try:
   
    with open(file_path, "rb") as file:
        file_data = file.read()
        file_name = file.name

 
    msg.add_attachment(
        file_data,
        maintype="text",
        subtype="plain",
        filename="basics.txt"
    )
    server = smtplib.SMTP("smtp.gmail.com",587)

    server.starttls()

    server.login(
        sender_email,
        password
    )

    server.send_message(msg)

    print("Email with attachment sent successfully")

    server.quit()

except Exception as e:
    print("Error:", e)
