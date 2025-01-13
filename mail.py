import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email_notification(sender_email, sender_password, recipient_email, subject, message_body):
    try:
        # Create the email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Attach the message body
        msg.attach(MIMEText(message_body, 'plain'))

        # Connect to the SMTP server
        smtp_server = "smtp.gmail.com"  # Use appropriate SMTP server for your email provider
        smtp_port = 587  # Common port for SMTP with TLS

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            # Start TLS encryption
            server.starttls()

            # Login to the email account
            server.login(sender_email, sender_password)

            # Send the email
            server.send_message(msg)

        print("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email: {e}")

# Example usage
if __name__ == "__main__":
    sender_email = "soumyaroyrdx@gmail.com"  # Replace with your email
    sender_password = "cxyl inyc osra mkvl"       # Replace with your email password or app-specific password
    recipient_email = "soumyaroyrdx@gmail.com"  # Replace with recipient's email
    subject = "Notification: Task Completed"
    message_body = "Hello,\n\nYour task has been successfully completed.\n\nBest regards,\nYour Team"

    send_email_notification(sender_email, sender_password, recipient_email, subject, message_body)