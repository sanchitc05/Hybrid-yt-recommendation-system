# Hybrid YouTube Video Recommendation System

## Overview
This project implements a hybrid recommendation system for an AI-integrated e-learning platform. The system leverages the YouTube Data API to fetch relevant video content based on user-inputted keywords. It combines content-based filtering by retrieving video data directly from YouTube with collaborative filtering methods for future expansion.

## Features
- **Keyword-based Video Retrieval**: Users can enter keywords, and the system fetches the top 5 relevant YouTube videos.
- **Hybrid Recommendation**: Combines content-based and collaborative filtering approaches for more comprehensive recommendations.
- **Easy to Use**: The code is designed to be run in a Google Colab notebook, making it accessible for educational and development purposes.

## Prerequisites
Before running the code, ensure you have:
- A Google account to create a project in the [Google Cloud Console](https://console.cloud.google.com/).
- Enabled the YouTube Data API v3 for your project.
- Generated an API key and replaced it in the code.

## Installation
To set up the project, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/sanchitc05/Hybrid-yt-recommendation-system.git
   cd hybrid-yt-recommendation-system
   ```

2. **Install Required Libraries**:
   Make sure you have the following libraries installed. You can run this command in your Google Colab notebook:
   ```python
   !pip install google-api-python-client
   ```

## Usage
1. Open the notebook in Google Colab.
2. Replace the placeholder `'YOUR_API_KEY'` in the code with your actual YouTube API key.
3. Run the cells in the notebook.
4. When prompted, enter a keyword related to the video content you want to find.

## Code Structure
- `hybrid_recommendation.py`: Contains the main logic for fetching YouTube videos based on keywords.
- `requirements.txt`: Lists the necessary Python libraries for the project.

## Future Work
- Implement a more robust collaborative filtering algorithm with real user data.
- Enhance user interface for better interaction.
- Expand the dataset for more diverse recommendations.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- The YouTube Data API for providing access to video data.
- The Surprise library for collaborative filtering techniques.

## Contact
For any inquiries, please contact:
- **Name**: Sanchit Chauhan
- **Email**: sanchitchauhan005@gmail.com
