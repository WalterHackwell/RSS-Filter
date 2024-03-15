from flask import Flask, render_template
import feedparser

app = Flask(__name__)

# List of RSS feeds to parse
FEEDS = ['https://www.nu.nl/rss']  # Replace this with the actual RSS feed URLs

# Keywords to filter the RSS feed entries
KEYWORDS = ['Treinstoring', "treinstoring", "Spoorweg", "Spoorwegen", "spoorweg", "spoorwegen", "vertraging"]

def get_entry_attribute(entry, attribute):
    """
    Safely get an attribute from a feed entry.
    Returns the attribute value if it exists, otherwise returns an empty string.
    """
    return getattr(entry, attribute, '')

@app.route('/')
def home():
    filtered_entries = []
    for feed_url in FEEDS:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries:
            title = get_entry_attribute(entry, 'title')
            summary = get_entry_attribute(entry, 'summary')
            
            # Check if any of the keywords exist in the title or summary
            if any(keyword in title for keyword in KEYWORDS) or any(keyword in summary for keyword in KEYWORDS):
                filtered_entries.append(entry)
    
    return render_template('index.html', entries=filtered_entries)

if __name__ == '__main__':
    app.run(debug=True)