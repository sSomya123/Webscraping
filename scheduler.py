import schedule
import time
from emailautomate import send_email 


def send_scraped_data_email():
    subject = "Scraped Data"
    body = "Please find the attached scraped data files."
    attachment_paths = ["data/scraped_page.html", "data/scraped_headings.html", "data/scraped_links.html", "data/scraped_imgs.html"]
    send_email(subject, body, attachment_paths)


schedule.every().day.at("09:00").do(send_scraped_data_email)

print("Scheduler is running. It will send an email every day at 9 AM.")


while True:
    schedule.run_pending()
    time.sleep(60)  
