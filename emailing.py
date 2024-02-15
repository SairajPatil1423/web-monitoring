import imghdr
import smtplib
from email.message import EmailMessage


password = "amclyhmnoufqpqnv"
def send_email(img_path):
    print("sending email")
    email_msg = EmailMessage()
    email_msg["Subject"]= "customer catched"
    email_msg.set_content("we got a customer!")
    with open(img_path,"rb") as file:
        content = file.read()
    email_msg.add_attachment(content,maintype="image",subtype =imghdr.what(file, content))

    gmail = smtplib.SMTP("smtp.gmail.com",587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login("sairajpatil1423@gmail.com",password)
    gmail.sendmail("sairajpatil1423@gmail.com","sairajpatil1423@gmail.com", email_msg.as_string())
    gmail.quit()
    print("email sent")

if __name__ == "__main__":
    send_email(img_path="images/1.png")