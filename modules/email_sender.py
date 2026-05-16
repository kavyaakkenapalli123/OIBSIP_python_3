import smtplib

EMAIL = "your_email@gmail.com"

PASSWORD = "your_password"

def send_email():

    receiver = "receiver@gmail.com"

    message = "Hello from Voice Assistant"

    server = smtplib.SMTP("smtp.gmail.com", 587)

    server.starttls()

    server.login(EMAIL, PASSWORD)

    server.sendmail(
        EMAIL,
        receiver,
        message
    )

    server.quit()