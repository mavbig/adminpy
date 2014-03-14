__author__ = 'mAvbig'

import re

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    if USER_RE.match(username):
        return username
    #return username and USER_RE.match(username)

PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    if PASS_RE.match(password):
        return password
    #return password and PASS_RE.match(password)

EMAIL_RE  = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
def valid_email(email):
    if EMAIL_RE.match(email):
        return  email
    #return not email or EMAIL_RE.match(email)

NAME_RE = re.compile(r"^[a-zA-Z0-9_-]{2,50}$")
def valid_name(name):
    if NAME_RE.match(name):
        return name