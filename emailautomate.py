import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

def send_email(subject, body, attachment_paths):
    # Email server details
    sender_email = "technologyindiatechnologyindia@gmail.com"  # Replace with your email
    receiver_email = "nobodysomya@gmail.com"  # Replace with the recipient's email
    password = "fhzy xrvb dbzz vfri"  # Replace with your email password (or app-specific password)

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Add the body to the email
    msg.attach(MIMEText(body, 'plain'))

    # Attach any files (scraped data files)
    for file_path in attachment_paths:
        if os.path.exists(file_path):
            with open(file_path, 'rb') as file:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(file.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(file_path)}')
                msg.attach(part)
        else:
            print(f"File {file_path} not found, skipping attachment.")

    # Send the email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:  # You can use your email provider's SMTP server
            server.starttls()  # Secure connection
            server.login(sender_email, password)
            text = msg.as_string()
            server.sendmail(sender_email, receiver_email, text)
            print(f"Email sent to {receiver_email} successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")

# Example usage
subject = "Scraped Data"
body = "Please find the attached scraped data files."
attachment_paths = ["data/scraped_page.html", "data/scraped_headings.html", "data/scraped_links.html", "data/scraped_imgs.html"]

send_email(subject, body, attachment_paths)
