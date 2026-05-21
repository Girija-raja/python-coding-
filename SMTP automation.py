from datetime import datetime
from email.message import EmailMessage
import os
import shutil
import smtplib
import time
sender_email = "1234@gmail.com"
password = "gfhf skjs sshk shuh"
receiver_email = "1234@gmail.com"
source_dir = r"D:/abc/day 1"  
temp_today_dir = r"D:/abc/day 1/today_files"  
zip_output_base = r"D:/abc/day 1/basics"  
file_to_send = r"D:/abc/day 1/basics.zip"

TARGET_TIME = "15:38"
already_sent_today = False
current_day = datetime.now().strftime("%Y-%m-%d")

print(
    f"Automation Active. Monitoring files to send daily ZIP at {TARGET_TIME}..."
)
while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    today_date = now.strftime("%Y-%m-%d")

    if today_date != current_day:
        current_day = today_date
        already_sent_today = False
    if current_time == TARGET_TIME and not already_sent_today:
        print(f"\nTime matched ({current_time}). Processing today's files...")

        try:
            if os.path.exists(temp_today_dir):
                shutil.rmtree(temp_today_dir)
            os.makedirs(temp_today_dir)
            files_found_today = 0
            if os.path.exists(source_dir):
                for item in os.listdir(source_dir):
                    item_path = os.path.join(source_dir, item)
                    if (
                        os.path.isfile(item_path)
                        and item_path != file_to_send
                        and "today_files" not in item_path
                    ):

                        file_timestamp = os.path.getmtime(item_path)
                        file_date = datetime.fromtimestamp(
                            file_timestamp
                        ).strftime("%Y-%m-%d")
                        if file_date == today_date:
                            shutil.copy(item_path, temp_today_dir)
                            files_found_today += 1
            else:
                raise FileNotFoundError(
                    f"Source directory {source_dir} does not exist."
                )
            if files_found_today > 0:
                print(
                    f"Found {files_found_today} files created today. Zipping..."
                )
                shutil.make_archive(zip_output_base, "zip", temp_today_dir)

                msg = EmailMessage()
                msg["Subject"] = f"Daily Automated Zip Report - {today_date}"
                msg["From"] = sender_email
                msg["To"] = receiver_email
                msg.set_content(
                    f"Hello!\n\nPlease find attached a ZIP archive containing the {files_found_today} file(s) created or modified today ({today_date})."
                )
                with open(file_to_send, "rb") as file:
                    file_data = file.read()

                msg.add_attachment(
                    file_data,
                    maintype="application",
                    subtype="zip",
                    filename=f"files_{today_date}.zip",
                )

                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(sender_email, password)
                server.send_message(msg)
                server.quit()

                print(f"Success: Email containing zip sent at {current_time}.")
            else:
                print(
                    f"No new files were created or modified today ({today_date}). Email skipped."
                )
            if os.path.exists(temp_today_dir):
                shutil.rmtree(temp_today_dir)
            already_sent_today = True

        except Exception as e:
            print(f"Automation error encountered: {e}")
            print("The script will remain active to try again tomorrow.")
    time.sleep(30)
