#!/usr/bin/env python3
"""
Python script to check what books are on offer for packt today. It sends the
link to download if it meets criteria.
"""
import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from requests_html import HTMLSession

from env import envar

logging.basicConfig(level=logging.DEBUG)


def main():
    program = Packtpull()
    program.run()


class Packtpull:
    """Pull down packt's free ebook."""

    def __init__(self):
        self.url = 'https://www.packtpub.com//packt/offers/free-learning'
        self.matches = ['python', 'go', 'golang', 'devops']
        self.email_account = envar.EMAIL_USERNAME
        self.email_password = envar.EMAIL_PASSWORD
        self.recipient = envar.RECIPIENT

    def check_title(self):
        session = HTMLSession()
        resp = session.get(self.url)
        title = resp.html.find("#title-bar-title", first=True)
        return title.text

    def worth_keeping(self):
        title = self.check_title()
        words = [x.lower() for x in title.split()]
        logging.info(f" {title} Currently Available.")
        for word in words:
            if word in self.matches:
                self.send_email(title)

    def send_email(self, title):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.set_debuglevel(1)
        server.starttls()
        server.login(self.email_account, self.email_password)
        msg = MIMEMultipart()
        msg['From'] = self.email_account
        msg['To'] = self.recipient
        msg['Subject'] = title
        text = f"""
        <body>
        <h1> {title} </h1>
        <p>Link to sign in and download eBook</p>
        <a href='{self.url}'>Click Here</a>
        </body>
        """
        msg.attach(MIMEText(text, 'html'))
        server.sendmail(self.email_account, self.recipient, msg.as_string())
        server.quit()

    def run(self):
        return self.worth_keeping()


if __name__ == '__main__':
    main()
