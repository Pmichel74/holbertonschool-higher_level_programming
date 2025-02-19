#!/usr/bin/python3
"""Module for fetching and processing posts from JSONPlaceholder API"""
import csv
import requests


def fetch_and_print_posts():
    """Function that fetches posts and prints their titles
    Makes a GET request to JSONPlaceholder API
    Prints the status code and all post titles"""
    url = "https://jsonplaceholder.typicode.com/posts"  # API endpoint

    try:
        # Attempt to fetch data from API
        res = requests.get(url)
        res.raise_for_status()  # Check for HTTP errors (4xx, 5xx)
    except requests.RequestException as e:
        print(f"Failed to retrieve data: {e}")
        return

    # Display HTTP status code
    print("Status Code: {}".format(res.status_code))

    # Process JSON data if content type is correct
    if res.headers.get("Content-Type") == "application/json; charset=utf-8":
        json_data = res.json()  # Parse JSON response
        for post in json_data:
            print(post["title"])  # Print each post's title


def fetch_and_save_posts():
    """Function that fetches posts and saves them to a CSV file
    1. Fetches posts from JSONPlaceholder API
    2. Filters required fields (id, title, body)
    3. Saves data to posts.csv"""
    url = "https://jsonplaceholder.typicode.com/posts"  # API endpoint

    try:
        # Attempt to fetch data from API
        res = requests.get(url)
    except requests.RequestException as e:
        print(f"Failed to retrieve data: {e}")
        return

    # Parse JSON response
    json_data = res.json()
    csvfile = "posts.csv"  # Output file name

    # Filter and format the data
    filtered_data = [
        {key: post[key] for key in ('id', 'title', 'body')}  # Keep only required fields
        for post in json_data
    ]
    headers = ['id', 'title', 'body']  # CSV column headers

    # Write data to CSV file
    with open(csvfile, "w", newline="") as file:
        csv_write = csv.DictWriter(file, fieldnames=headers)
        csv_write.writeheader()  # Write column headers
        csv_write.writerows(filtered_data)  # Write all posts
