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

### Downloading the Application
Clone the application from its repository or download the source code directly to your local machine.

### Running the Application
Navigate to the application directory in your terminal or command prompt and run the application with the following command:
```
python app.py
```
By default, the application will run on http://127.0.0.1:5000/. Open this URL in your web browser to view the filtered RSS feed entries.

### Configuration
RSS Feeds
Modify the FEEDS list in app.py to include the URLs of the RSS feeds you want to parse. By default, it is set to a single feed for demonstration purposes:

```
FEEDS = ['https://www.nu.nl/rss']  # Replace with actual RSS feed URLs
```

### Keywords
The KEYWORDS list contains the keywords used to filter feed entries. Update this list based on your filtering needs:

```
KEYWORDS = ['Treinstoring', "treinstoring", "Spoorweg", "Spoorwegen", "spoorweg", "spoorwegen", "vertraging"]
```

### Usage
After starting the application, it will automatically parse the specified RSS feeds and filter the entries based on the defined keywords. The filtered entries will be displayed on the homepage of the web application.

### Customization
You can customize the appearance of the web page by editing the templates/index.html file. Additionally, the keyword filtering logic can be adjusted or expanded in the home function within app.py.

### Support
For support, open an issue in the repository or contact the developer directly.


