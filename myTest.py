import requests
import os
import re
import string
from bs4 import BeautifulSoup
import logging
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist
from nltk.util import ngrams
import telepot
import notion_client

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

def start(update: Update, context: CallbackContext):
    """Send a message when the command /start is issued."""
    update.message.reply_text("Hi there! How can I help you today?")

def help_command(update: Update, context: CallbackContext):
    """Send a message when the command /help is issued."""
    update.message.reply_text("I am here to help you find the latest summarized newsletter data! "
                              "You can query the latest newsletter using /newsletter.")

def newsletter(update: Update, context: CallbackContext):
    """Crawl the email newsletter data, extract and summarize key context, and send it to Notion page and Telegram."""
    # Get the email newsletter data
    html_page = requests.get("https://example.com/newsletter")
    soup = BeautifulSoup(html_page.content, "html.parser")
    text = soup.get_text()

    # Preprocess the data
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text)
    words = [word.lower() for word in words if word not in string.punctuation]
    words = [word for word in words if word not in stop_words]

    # Extract key phrases and summarize the content
    n = 2
    ngrams = ngrams(words, n)
    fdist = FreqDist(ngrams)
    top_ngrams = fdist.most_common(10)

    # Send the summarized data to Notion
    client = notion