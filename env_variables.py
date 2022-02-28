#!/bin/python3
import os 
user = os.environ.get('USER')
#print(user)

shell = os.environ.get('SHELL')
#print(shell)


print(f'Hello {user}')



