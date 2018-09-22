#!/usr/bin/env python3
"""
Python script to check what books are on offer for packt today. It sends the
link to download if it meets criteria.
"""
import logging

from requests_html import HTMLSession

logging.basicConfig(level=logging.DEBUG)


def main():
    program = Packtpull()
    program.run()


class Packtpull:
    """Pull down packt's free ebook."""

    def __init__(self):
        self.url = 'https://www.packtpub.com//packt/offers/free-learning'
        self.matches = ['python', 'go', 'golang', 'devops']

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
                # logic here that alerts if in list.
                print(f'{word} found!')

    def run(self):
        return self.worth_keeping()


if __name__ == '__main__':
    main()
