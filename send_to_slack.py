#!/usr/bin/env python3

import argparse
import os
import re
import sys
import logging
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def convert_markdown_to_slack(content):
    logger.debug("Converting markdown to Slack format")
    # Convert headers
    content = re.sub(r'^# (.*)$', r'*:large_blue_diamond: \1*', content, flags=re.MULTILINE)
    content = re.sub(r'^## (.*)$', r'*\1*', content, flags=re.MULTILINE)
    content = re.sub(r'^### (.*)$', r'*\1*', content, flags=re.MULTILINE)
    
    # Convert links [text](url) to <url|text>
    content = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<\2|\1>', content)
    
    # Convert bold **text** to *text*
    content = re.sub(r'\*\*([^*]+)\*\*', r'*\1*', content)
    
    # Convert italic *text* to _text_
    content = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'_\1_', content)
    
    # Convert code blocks
    content = re.sub(r'```([^`]+)```', r'```\1```', content)
    
    # Convert inline code
    content = re.sub(r'`([^`]+)`', r'`\1`', content)
    
    # Convert lists - preserve indentation for multi-level lists
    content = re.sub(r'^(\s*)[-*] ', r'\1- ', content, flags=re.MULTILINE)
    
    return content

def read_file(file_path):
    logger.info(f"Reading file: {file_path}")
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            logger.debug(f"Successfully read {len(content)} characters from file")
            return content
    except FileNotFoundError:
        logger.error(f"File '{file_path}' not found")
        raise
    except Exception as e:
        logger.error(f"Error reading file: {e}")
        raise

def extract_title_and_content(content):
    """Extract the title (first line starting with #) and the rest of the content"""
    lines = content.split('\n')
    title = None
    rest_content = []
    
    for line in lines:
        if line.startswith('# ') and title is None:
            title = line[2:].strip()  # Remove the # and space
        else:
            rest_content.append(line)
    
    return title, '\n'.join(rest_content)

def send_to_slack(client, content, channel, thread_ts=None):
    logger.info("Preparing to send message to Slack")
    try:
        # Convert markdown to Slack formatting
        logger.debug("Converting markdown to Slack format")
        slack_content = convert_markdown_to_slack(content)
        
        # Send message using Web API
        response = client.chat_postMessage(
            channel=channel,
            text=slack_content,
            thread_ts=thread_ts
        )
        
        logger.info("Successfully sent message to Slack!")
        return response["ts"]  # Return the message timestamp
    except SlackApiError as e:
        logger.error(f"Error sending message to Slack: {e.response['error']}")
        raise

def main():
    parser = argparse.ArgumentParser(description='Send team updates to Slack')
    parser.add_argument('--input_file', required=True, help='Path to the input markdown file')
    parser.add_argument('--channel', required=True, help='Slack channel to send message to')
    parser.add_argument('--thread_ts', help='Thread timestamp to reply to an existing message')
    parser.add_argument('--use_thread', action='store_true', help='Send title first, then rest in thread')
    parser.add_argument('--debug', action='store_true', help='Enable debug logging')
    args = parser.parse_args()

    if args.debug:
        logger.setLevel(logging.DEBUG)
        logger.debug("Debug logging enabled")

    # Initialize Slack client
    slack_token = os.getenv('SLACK_BOT_TOKEN')
    if not slack_token:
        logger.error("SLACK_BOT_TOKEN environment variable is not set")
        raise ValueError("SLACK_BOT_TOKEN environment variable is not set")

    client = WebClient(token=slack_token)

    content = read_file(args.input_file)
    
    if args.use_thread:
        # Extract title and rest of content
        title, rest_content = extract_title_and_content(content)
        if not title:
            logger.error("No title found in markdown file (first line should start with #)")
            raise ValueError("No title found in markdown file (first line should start with #)")
            
        # Send title first
        logger.info("Sending title message...")
        thread_ts = send_to_slack(client, title, args.channel)
        
        # Send rest of content in thread
        logger.info("Sending rest of content in thread...")
        send_to_slack(client, rest_content, args.channel, thread_ts)
    else:
        # Send entire content as one message
        send_to_slack(client, content, args.channel, args.thread_ts)

if __name__ == '__main__':
    load_dotenv() # Load .env file when script is run directly
    main() 