import getpass
import smtplib

HOST = "smtp-mail.outlook.com"
PORT = 587

FROM_EMAIL = "from_email"
TO_EMAIL = "to_email"

PASSWORD = getpass.getpass("Enter Password")

MESSAGE = """Subject: Mail sent using python
Hi Goku,

anuj here found the four star dragon ball!.

Thanks,
Test Account"""


smtp = smtplib.SMTP(HOST, PORT)

status_code, response = smtp.ehlo()
print(f"[*] Echoing the server: {status_code}{response}")

status_code, response = smtp.starttls()
print(f"[*] Starting TLS connection: {status_code}{response}")


status_code, response = smtp.login(FROM_EMAIL, PASSWORD)
print(f"[*] Logging in: {status_code}{response}")


smtp.sendmail(FROM_EMAIL, TO_EMAIL, MESSAGE)

smtp.close()
