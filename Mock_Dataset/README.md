# Social Media Engagement Mock Dataset Generator

This project generates a mock dataset for social media posts, including engagement metrics such as likes, shares, and comments. The dataset simulates a year of social media activity, taking into account different types of posts (carousel, reel, static image) and seasonal trends such as holidays and special events. The dataset is saved in both JSON and CSV formats.

## Features
- **Post Types**: The generator includes three types of posts:
  - Carousel
  - Reel
  - Static Image
  
- **Engagement Profiles**: Each post type has an associated range for likes, shares, and comments, based on realistic engagement data for each post type.
  - Carousel: 100-300 likes, 10-50 shares, 20-80 comments
  - Reel: 200-500 likes, 50-150 shares, 100-250 comments
  - Static Image: 50-150 likes, 5-20 shares, 10-40 comments
  
- **Event-based Engagement Spikes**: Special events throughout the year (e.g., Valentine's Day, Independence Day, Halloween) cause engagement to spike. These events modify engagement metrics for the posts published on these dates.

- **Noise in Engagement Metrics**: A small random noise is introduced to simulate anomalies in social media behavior. This includes:
  - **Viral Posts**: 5% chance for a post to have a significantly higher-than-normal engagement.
  - **Low-performing Posts**: 5% chance for a post to have very low engagement.

- **Post Distribution**: The generator varies the number of posts per day based on the month, with more posts in peak months like November and December, and fewer posts during the summer months.

## Files Generated
The project generates the following files:
- **JSON**: `mock_engagement_data.json` – A file containing the generated dataset in JSON format.
- **CSV**: `mock_engagement_data.csv` – A file containing the generated dataset in CSV format.

## How It Works
1. **Post Count by Date**: The generator determines the number of posts per day for each day of the year, based on seasonal trends.
2. **Post Generation**: For each post, the generator randomly selects a post type and generates engagement data (likes, shares, comments) based on the selected post type and potential event spikes.
3. **Noise Injection**: Random noise is added to the engagement data to simulate viral and low-performing posts.
4. **Save to Files**: The generated data is saved to both JSON and CSV files.

## Installation and Usage

### Requirements
- Python 3.x

### Steps
1. Clone or download this repository.

2. Run the script to generate the mock dataset:
   ```bash
   python generate_mock_data.py
   ```

3. The script will generate the dataset and save it to `mock_engagement_data.json` and `mock_engagement_data.csv` in the same directory.

## Sample Output

Example entry in the generated dataset:
```json
{
  "post_id": 1,
  "post_type": "carousel",
  "likes": 320,
  "shares": 30,
  "comments": 50,
  "created_at": "2024-03-17 14:30:00"
}
```

## Customization
You can modify the following parameters in the code:
- **POST_TYPES**: Add or remove post types as needed.
- **ENGAGEMENT_PROFILES**: Adjust the ranges for likes, shares, and comments for different post types.
- **EVENTS**: Add more events or modify existing ones to change the engagement spikes for specific dates.

## Conclusion
This project provides a flexible and customizable way to generate mock social media engagement data for testing or analysis purposes. By simulating different post types, seasonal trends, and engagement anomalies, the dataset can be used for various scenarios in social media analytics, marketing research, and more.