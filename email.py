import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_mail(file_path, mail):

    smtp_server = "smtp-mail.outlook.com"
    smtp_port = 587 
    smtp_username = "email"
    smtp_password = "pwd"

    message = MIMEMultipart()
    message["From"] = "email"
    message["To"] = mail
    message["Subject"] = f"{file_path} Scraped file"

    message.attach(MIMEText("test", "plain"))

    file_name = file_path[2:]

    attachment = open(file_path, "rb")

    mime_base = MIMEBase("application", "octet-stream")
    mime_base.set_payload(attachment.read())
    attachment.close()

    encoders.encode_base64(mime_base)

    mime_base.add_header("Content-Disposition", f"attachment; filename= {file_name}",)

    message.attach(mime_base)

    try:
        context = smtplib.SMTP(smtp_server, smtp_port)
        context.starttls() 
        context.login(smtp_username, smtp_password)  # Login

        # Send email
        context.sendmail("email", mail, message.as_string())
        print("Email Ersal Shod!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        context.quit()

