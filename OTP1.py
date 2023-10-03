import os
import secrets
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Function to generate a random 6-digit OTP
def generate_otp():
    return ''.join(secrets.choice("0123456789") for _ in range(6))


# Function to send an email with OTP
def send_email_with_otp(sender_email, sender_password, recipient_email, otp):
    try:
        smtp_server = "smtp.gmail.com"
        smtp_port = 587

        # Create an SMTP object and establish a connection
        s = smtplib.SMTP(smtp_server, smtp_port)
        s.starttls()
        s.login(sender_email, sender_password)

        subject = "Your OTP"
        body = f"Your OTP is: {otp}"

        # Create a multipart message and set its headers
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = recipient_email
        msg["Subject"] = subject

        # Attach the OTP message as plain text
        msg.attach(MIMEText(body, "plain"))

        # Send the email
        s.sendmail(sender_email, recipient_email, msg.as_string())
        print("OTP sent successfully!")

        # Close the SMTP connection
        s.quit()
    except smtplib.SMTPException as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    sender_email = "spmb5478@gmail.com"  # Replace with your Gmail email address
    sender_password = "your_password"  # Replace with your Gmail app password

    recipient_email = input("Enter your email: ")
    otp = generate_otp()

    send_email_with_otp(sender_email, sender_password, recipient_email, otp)

    user_input = input("Enter Your OTP >>: ")

    if user_input == otp:
        print("Verified")
    else:
        print("Please Check your OTP again")
