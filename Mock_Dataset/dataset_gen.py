import json
import random
import csv
from datetime import datetime, timedelta

# Define post types and realistic engagement distributions
POST_TYPES = ["carousel", "reel", "static_image"]
ENGAGEMENT_PROFILES = {
    "carousel": {"likes": (100, 300), "shares": (10, 50), "comments": (20, 80)},
    "reel": {"likes": (200, 500), "shares": (50, 150), "comments": (100, 250)},
    "static_image": {"likes": (50, 150), "shares": (5, 20), "comments": (10, 40)}
}

# Define event-based engagement spikes
EVENTS = {
    "2024-02-14": {"likes": (500, 1000), "shares": (100, 300), "comments": (200, 500)},  # Valentine's Day
    "2024-03-17": {"likes": (400, 900), "shares": (90, 250), "comments": (180, 450)},   # St. Patrick's Day
    "2024-07-04": {"likes": (600, 1200), "shares": (120, 350), "comments": (250, 600)}, # Independence Day
    "2024-10-31": {"likes": (450, 900), "shares": (100, 300), "comments": (200, 500)},  # Halloween
    "2024-11-28": {"likes": (400, 800), "shares": (80, 200), "comments": (150, 400)},   # Thanksgiving
    "2024-12-25": {"likes": (600, 1200), "shares": (150, 400), "comments": (300, 700)}, # Christmas
    "2024-12-31": {"likes": (700, 1300), "shares": (200, 500), "comments": (350, 800)}  # New Year's Eve
}

# Define post distribution over the year
def posts_count_by_date():
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 12, 31)
    current_date = start_date
    posts_by_date = []

    while current_date <= end_date:
        if current_date.month in [11, 12] or current_date.month == 1:  # Peak months for holidays
            posts_today = random.randint(5, 15)
        elif current_date.month in [6, 7, 8]:  # Summer dip
            posts_today = random.randint(1, 5)
        else:  # Average months
            posts_today = random.randint(3, 10)

        posts_by_date.extend([current_date] * posts_today)
        current_date += timedelta(days=1)

    random.shuffle(posts_by_date)
    return posts_by_date

# Function to introduce noise into engagement metrics
def add_noise_to_engagement(likes, shares, comments):
    anomaly_chance = random.random()
    if anomaly_chance < 0.05:  # 5% chance for a viral post
        likes *= random.randint(2, 5)
        shares *= random.randint(3, 7)
        comments *= random.randint(2, 6)
    elif anomaly_chance < 0.10:  # 5% chance for a low-performing post
        likes = max(1, likes // random.randint(2, 5))
        shares = max(1, shares // random.randint(2, 4))
        comments = max(1, comments // random.randint(2, 4))
    return likes, shares, comments

# Function to generate a single post
def generate_post(post_id, post_date):
    post_date_str = post_date.strftime("%Y-%m-%d")
    if post_date_str in EVENTS:  # Check if the date has a special event
        engagement = EVENTS[post_date_str]
        likes = random.randint(*engagement["likes"])
        shares = random.randint(*engagement["shares"])
        comments = random.randint(*engagement["comments"])
    else:
        post_type = random.choice(POST_TYPES)
        engagement = ENGAGEMENT_PROFILES[post_type]
        likes = random.randint(*engagement["likes"])
        shares = random.randint(*engagement["shares"])
        comments = random.randint(*engagement["comments"])

        # Add noise to engagement metrics
        likes, shares, comments = add_noise_to_engagement(likes, shares, comments)

    return {
        "post_id": post_id,
        "post_type": "event" if post_date_str in EVENTS else random.choice(POST_TYPES),
        "likes": likes,
        "shares": shares,
        "comments": comments,
        "created_at": post_date.strftime("%Y-%m-%d %H:%M:%S")
    }

# Generate mock dataset
def create_mock_dataset():
    posts_by_date = posts_count_by_date()
    dataset = [generate_post(post_id, post_date) for post_id, post_date in enumerate(posts_by_date, start=1)]
    return dataset

# Save dataset to a JSON file
def save_to_json(data, filename="mock_engagement_data.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

# Save dataset to a CSV file
def save_to_csv(data, filename="mock_engagement_data.csv"):
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["post_id", "post_type", "likes", "shares", "comments", "created_at"])
        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    # Generate dataset
    mock_data = create_mock_dataset()

    # Save the data to JSON and CSV files
    save_to_json(mock_data)
    save_to_csv(mock_data)

    print("Mock dataset generated and saved to 'mock_engagement_data.json' and 'mock_engagement_data.csv'")
