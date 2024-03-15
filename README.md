# RSS Feed Filter: README

## Overview
This Python Flask application filters RSS feed entries based on specific keywords. It uses the `feedparser` library to parse RSS feeds and the Flask framework to display the filtered entries on a web page. The application is designed to filter news articles that mention specific keywords related to train disruptions, delays, and railway news in general, making it easier for users to find relevant updates.

## Features
- **RSS Feed Parsing**: Utilizes `feedparser` to parse RSS feeds from specified URLs.
- **Keyword Filtering**: Filters feed entries based on a predefined list of keywords related to train disruptions and railway news.
- **Web Interface**: Displays the filtered feed entries on a web page using Flask.

## Installation

### Prerequisites
Ensure you have Python installed on your system. This application was developed with Python 3.8. It may work with other versions but is not guaranteed.

### Dependencies
The application requires Flask and feedparser. Install them using pip:

```bash
pip install Flask feedparser
```
