import os
import snowflake.connector
import requests
from bs4 import BeautifulSoup

# ----------------------------
# Snowflake Connection
# ----------------------------
def get_snowflake_connection():
    """Establish a secure Snowflake connection using environment variables."""
    return snowflake.connector.connect(
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
        database=os.getenv("SNOWFLAKE_DATABASE"),
        schema=os.getenv("SNOWFLAKE_SCHEMA")
    )

# ----------------------------
# Scrape Clubs from Website
# ----------------------------
def fetch_clubs_from_website(url):
    """Fetch club data from the university website."""
    clubs = []
    while url:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        # Adjust selectors according to page structure
        club_elements = soup.select(".org-card")  # Example CSS selector
        for club in club_elements:
            name = club.select_one(".org-card__title").text.strip()
            category = club.select_one(".org-card__category").text.strip()
            description = club.select_one(".org-card__description").text.strip()
            clubs.append((name, description, category))

        # Pagination (example)
        next_page = soup.select_one("a.next")
        url = next_page['href'] if next_page else None

    return clubs

# ----------------------------
# Save Clubs to Snowflake
# ----------------------------
def save_clubs_to_snowflake(clubs):
    """Save club data into Snowflake table."""
    conn = get_snowflake_connection()
    cur = conn.cursor()

    # Create table if not exists
    cur.execute("""
        CREATE TABLE IF NOT EXISTS CLUBS (
            name STRING,
            description STRING,
            category STRING
        )
    """)

    # Optional: Clear previous entries
    cur.execute("TRUNCATE TABLE CLUBS")

    # Insert clubs
    for club in clubs:
        cur.execute(
            "INSERT INTO CLUBS (name, description, category) VALUES (%s, %s, %s)",
            club
        )

    cur.close()
    conn.close()
    print(f"✅ {len(clubs)} clubs saved to Snowflake")
