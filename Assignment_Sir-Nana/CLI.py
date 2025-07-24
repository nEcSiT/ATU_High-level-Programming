#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import random
from person_data import MyData

"""
Created on Thu Oct 19 16:00:00 2023
Author: Nicholas Dornyo

A small command-line tool that asks the user some personal details and then displays a customized summary.

The program prompts the user for the following information:
- Their name
- Age
- Favorite color
- Favorite food
- City they live in
- SHS (Senior High School) attended
- Favourite soccer team
- Additional personal preferences

After collecting all the information, it displays a personalized summary of the user's details.
"""

print("Welcome to the Personal Details CLI!")

# Define questions with their corresponding attribute names
questions = [
    ("name", "What is your name? "),
    ("age", "How old are you? "),
    ("color", "What is your favorite color? "),
    ("food", "What is your favorite food? "),
    ("city", "Which city do you live in? "),
    ("shs", "Which Senior High School did you attend? "),
    ("soccer_team", "What is your favorite soccer team? "),
    ("hobbies", "What are some of your hobbies? "),
    ("dream_job", "What is your dream job? ")
]

# Shuffle the questions randomly
random.shuffle(questions)

# Collect user information in random order
user_data = {}
for attribute, question in questions:
    user_data[attribute] = input(question)

# Create MyData object with collected information
nicholas = MyData(
    name=user_data["name"],
    age=user_data["age"],
    color=user_data["color"],
    food=user_data["food"],
    city=user_data["city"],
    shs=user_data["shs"],
    soccer_team=user_data["soccer_team"],
    hobbies=user_data["hobbies"],
    dream_job=user_data["dream_job"]
)

# Display the summary of the collected information
print(
    f"\nThank you {nicholas.name} for sharing your details! Here is a summary of your information:\n"
    + nicholas.summary()
)