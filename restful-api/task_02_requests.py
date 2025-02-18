#!/usr/bin/python3
"""Module that defines a function to fetch posts from an API"""
import json
import requests
import csv


def fetch_and_print_posts():
    """Function that fetches posts and prints their titles"""
    url = "https://jsonplaceholder.typicode.com/posts"  # API endpoint URL

    try:
        # Make HTTP GET request and check response
        res = requests.get(url)
        res.raise_for_status()  # Raise exception for bad status codes
        json_data = res.json()  # Parse JSON response
    except requests.RequestException as e:
        print(f"Failed to retrieve data: {e}")
        return
    except json.JSONDecodeError as e:
        print(f"Failed to parse JSON: {e}")
        return

    print("Status Code: {}".format(res.status_code))

    # Only process if content is JSON
    if res.headers.get("Content-Type") == "application/json; charset=utf-8":
        for post in json_data:
            print(post["title"])


def fetch_and_save_posts():
    """Function that fetches posts and saves them to a CSV file"""
    url = "https://jsonplaceholder.typicode.com/posts"
    csvfile = "posts.csv"  # Output CSV filename

    try:
        # Fetch and parse data from API
        res = requests.get(url)
        res.raise_for_status()
        json_data = res.json()

        # Extract only needed fields from each post
        filtered_data = [{key: post[key] for key in ('id', 'title', 'body')}
                         for post in json_data]

        # Define CSV structure
        headers = ['id', 'title', 'body']

        # Write data to CSV file
        with open(csvfile, "w", newline="") as file:
            csv_write = csv.DictWriter(file, fieldnames=headers)
            csv_write.writeheader()  # Write column headers
            csv_write.writerows(filtered_data)  # Write post data

        print(f"Data successfully saved to {csvfile}")

    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return
    except json.JSONDecodeError as e:
        print(f"Failed to parse JSON: {e}")
        return
    except IOError as e:
        print(f"Failed to write to file: {e}")
        return
