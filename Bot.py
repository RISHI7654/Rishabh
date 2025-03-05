import os
import time
import requests
import json

# Facebook API URL for reactions, comments, etc.
GRAPH_API_URL = "https://graph.facebook.com/v11.0"

# Cookies-based Authentication (Replace with your cookies file path)
cookies_file = 'cookies.txt'

# Function to load cookies from the file
def load_cookies():
    cookies = {}
    with open(cookies_file, 'r') as file:
        for line in file.readlines():
            cookie_data = line.strip().split('=')
            if len(cookie_data) == 2:
                cookies[cookie_data[0]] = cookie_data[1]
    return cookies

# Auto React Function (Love, Angry, etc.)
def auto_react(post_id, reaction_type, cookies):
    url = f"{GRAPH_API_URL}/{post_id}/reactions"
    payload = {
        'access_token': cookies.get('access_token'),  # Access token from cookies
        'type': reaction_type
    }
    response = requests.post(url, data=payload, cookies=cookies)
    return response.json()

# Auto Comment Function
def auto_comment(post_id, message, cookies):
    url = f"{GRAPH_API_URL}/{post_id}/comments"
    payload = {
        'access_token': cookies.get('access_token'),
        'message': message
    }
    response = requests.post(url, data=payload, cookies=cookies)
    return response.json()

# Auto Poll Vote Function
def auto_poll_vote(poll_id, option_id, cookies):
    url = f"{GRAPH_API_URL}/{poll_id}/votes"
    payload = {
        'access_token': cookies.get('access_token'),
        'option_id': option_id
    }
    response = requests.post(url, data=payload, cookies=cookies)
    return response.json()

# Multi-Account Support (Load Facebook IDs and Page IDs)
def load_accounts():
    accounts = []
    with open('accounts.txt', 'r') as file:
        for line in file.readlines():
            account_details = line.strip().split(',')
            if len(account_details) == 3:  # Facebook ID, Page UID, and Cookies File
                accounts.append({
                    'facebook_id': account_details[0],
                    'page_uid': account_details[1],
                    'cookies_file': account_details[2]
                })
    return accounts

# Function to Display Logo
def display_logo():
    logo = """
    =======================
    |    INDRA BOT        |
    |     Version 1.0     |
    =======================
    """
    print(logo)

# Main Bot Function to Execute Actions
def run_bot():
    display_logo()  # Display the logo when the bot starts

    accounts = load_accounts()

    for account in accounts:
        # Load cookies for each account
        cookies = load_cookies()

        # Auto React to Post
        post_id = "post_id_here"  # Replace with actual Post ID
        auto_react(post_id, 'LOVE', cookies)
        print(f"Reacted to post {post_id} with LOVE.")

        # Auto Comment on Post
        message = "Great post!"
        auto_comment(post_id, message, cookies)
        print(f"Commented on post {post_id} with: {message}")

        # Auto Poll Vote
        poll_id = "poll_id_here"  # Replace with actual Poll ID
        option_id = "option_id_here"  # Replace with the option ID to vote for
        auto_poll_vote(poll_id, option_id, cookies)
        print(f"Voted on poll {poll_id} with option {option_id}.")

        # Add more actions here (e.g., auto-follow, auto-group join)

        # Sleep for 2 seconds before processing the next account
        time.sleep(2)

# Main Function to Start the Bot
if __name__ == '__main__':
    print("Starting Indra Bot...")
    run_bot()
