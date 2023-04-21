#!/usr/bin/python3

from fabric import task

@task
def hello(c):
    print("Hello, Motherfucker!")
