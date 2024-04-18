import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import string


def send_reset_password_email( email , NewPassword ):
  # Sender's email and password
  sender_email = "me@abdelrahman-nasr.tech"
  sender_password = "Cat9199@"  # Replace with the actual password
    # Generate a new random password
    subject = "Your New Password"
    html_body = f"""
<!doctype html>
<html lang="en-US">
<head>
    <meta content="text/html; charset=utf-8" http-equiv="Content-Type" />
    <title>New Password Email</title>
    <meta name="description" content="Your new password has been set.">
</head>
<body marginheight="0" topmargin="0" marginwidth="0" style="margin: 0px; background-color: #f2f3f8;" leftmargin="0">
    <table cellspacing="0" border="0" cellpadding="0" width="100%" bgcolor="#f2f3f8" style="@import url(https://fonts.googleapis.com/css?family=Rubik:300,400,500,700|Open+Sans:300,400,600,700); font-family: 'Open Sans', sans-serif;">
        <tr><td>
            <table style="background-color: #f2f3f8; max-width:670px; margin:0 auto;" width="100%" border="0" align="center" cellpadding="0" cellspacing="0">
                <tr><td style="height:80px;">&nbsp;</td></tr>
                <tr><td style="height:20px;">&nbsp;</td></tr>
                <tr><td>
                    <table width="95%" border="0" align="center" cellpadding="0" cellspacing="0" style="max-width:670px;background:#fff; border-radius:3px; text-align:center;-webkit-box-shadow:0 6px 18px 0 rgba(0,0,0,.06);-moz-box-shadow:0 6px 18px 0 rgba(0,0,0,.06);box-shadow:0 6px 18px 0 rgba(0,0,0,.06);">
                        <tr><td style="height:40px;">&nbsp;</td></tr>
                        <tr><td style="padding:0 35px;">
                            <h1 style="color:#1e1e2d; font-weight:500; margin:0;font-size:32px;font-family:'Rubik',sans-serif;">Your Password Has Been Reset</h1>
                            <p style="color:#455056; font-size:15px;line-height:24px; margin:0;">
                                Your new password is: <strong>{NewPassword}</strong><br>
                                Please use this new password to login and change it immediately for security purposes.
                            </p>
                        </td></tr>
                        <tr><td style="height:40px;">&nbsp;</td></tr>
                    </table>
                </td></tr>
                <tr><td style="height:20px;">&nbsp;</td></tr>
                <tr><td style="height:80px;">&nbsp;</td></tr>
            </table>
        </td></tr>
    </table>
</body>
</html>
    """

    # Create the MIME object
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = email
    message["Subject"] = subject

    # Attach the HTML body to the email
    message.attach(MIMEText(html_body, "html"))

    # Connect to the SMTP server
    try:
        with smtplib.SMTP("smtp.abdelrahman-nasr.tech", 587) as server:
            server.starttls()  # Use this line if using the STARTTLS protocol
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, email, message.as_string())
        print(f"Reset password email sent successfully to {email}")
    except Exception as e:
        print(f"Failed to send email: {e}")
