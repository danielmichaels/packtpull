# Packtpull

> A very simple python script that can be run each day to check Packt's daily
eBook offerings for interesting titles. 

Packtpull looks for certain titles and if found will email the user with a link
to login and download the eBook. Whilst not totally automated this really isn't
worth the rigmarole of paying for CAPTCHA breakers. Packtpull can be set via
a cron or another task scheduler.

## Usage

`python program.py`

Debugging is enabled which will output the SMTP information for quickly ascertaining
the cause of errors when executed from the terminal.

## Setup

This scripts uses the following convention to hide secrets:

Directory/module == `env/envar.py`

Within `envar.py` the following is searched for:
```shell
EMAIL_USERNAME='email address to send from'
EMAIL_PASSWORD='cheese and whiskers'
RECIPIENT='account that should receive the email'
```

## Search terms

By default the script will only fire if it finds a title with the following in
it:

- python
- go
- golang
- devops

## Email

The user must supply an email from which to send the email, and a recipient 
address. By default this uses gmail. 

It sends an email with very rudimentary HTML and a hyper link to the page from
which the user can then sign in and download the eBook.
