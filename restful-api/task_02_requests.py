#!/usr/bin/python3
"""Module that defines a function to fetch posts from an API"""
import json
import requests
import csv


def fetch_and_print_posts():
    """Fetches and prints posts from JSONPlaceholder"""
    url = "https://jsonplaceholder.typicode.com/posts"

    try:
        res = requests.get(url)
        res.raise_for_status()
        json_data = res.json()
    except requests.RequestException as e:
        print(f"Failed to retrieve data: {e}")
        return

    print("Status Code: {}".format(res.status_code))

    # Print titles only if request was successful
    if res.status_code == 200:
        for post in json_data:
            print(post["title"])


def fetch_and_save_posts():
    """Function that fetches posts and saves them to a CSV file"""
    url = "https://jsonplaceholder.typicode.com/posts"
    csvfile = "posts.csv"

    try:
        res = requests.get(url)
        res.raise_for_status()
        json_data = res.json()

        filtered_data = [{key: post[key] for key in ('id', 'title', 'body')}
                         for post in json_data]

        with open(csvfile, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(filtered_data)

    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return
    except json.JSONDecodeError as e:
        print(f"Failed to parse JSON: {e}")
        return
    except IOError as e:
        print(f"Failed to write to file: {e}")
        return
