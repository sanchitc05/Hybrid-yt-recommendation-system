from googleapiclient.discovery import build
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split
from surprise import accuracy
import pandas as pd
import numpy as np

# Replace with your YouTube API key
API_KEY = 'Your API key'

# Initialize YouTube API client
youtube = build('youtube', 'v3', developerKey=API_KEY)

# Function to fetch videos based on search query using YouTube API
def fetch_youtube_videos(query, max_results=5):
    request = youtube.search().list(
        part='snippet',
        q=query,
        type='video',
        maxResults=max_results
    )
    response = request.execute()
    videos = []
    for item in response['items']:
        video_info = {
            'title': item['snippet']['title'],
            'video_id': item['id']['videoId'],
            'description': item['snippet']['description']
        }
        videos.append(video_info)
    return videos

# Collaborative filtering example data (mock data for demonstration)
user_data = {
    'user_id': [1, 1, 2, 2, 3, 3],
    'video_id': [101, 102, 101, 103, 102, 104],
    'rating': [3, 5, 4, 2, 5, 3]
}
df_interactions = pd.DataFrame(user_data)

# Create a user-item interaction matrix
user_item_matrix = df_interactions.pivot_table(index='user_id', columns='video_id', values='rating').fillna(0)

# Prepare data for collaborative filtering
reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(df_interactions[['user_id', 'video_id', 'rating']], reader)
trainset, testset = train_test_split(data, test_size=0.2)

# Train collaborative filtering model
algo = SVD()
algo.fit(trainset)

# Content-based recommendations function
def content_based_recommendations(query, max_results=5):
    return fetch_youtube_videos(query, max_results)

# Collaborative filtering recommendations function
def collaborative_recommendations(user_id, max_results=5):
    predictions = []
    for video_id in user_item_matrix.columns:
        pred = algo.predict(user_id, video_id)
        predictions.append((video_id, pred.est))
    predictions.sort(key=lambda x: x[1], reverse=True)
    return [video_id for video_id, rating in predictions[:max_results]]

# Hybrid recommendation function
def hybrid_recommendations(user_id, query, max_results=5):
    # Get content-based recommendations
    content_recs = content_based_recommendations(query, max_results)

    # Get collaborative filtering recommendations
    collab_recs = collaborative_recommendations(user_id, max_results)

    # Combine recommendations, removing duplicates
    combined_recs = {rec['video_id']: rec for rec in content_recs}
    for video_id in collab_recs:
        combined_recs.setdefault(video_id, {'title': f"Video {video_id} (Collaborative Rec)", 'video_id': video_id, 'description': "Collaborative recommendation"})

    return list(combined_recs.values())[:max_results]

# Main function to prompt user and display hybrid recommendations
def main():
    query = input("Enter the keyword you want video about: ")
    user_id = int(input("Enter your user ID: "))  # For demonstration; replace with actual user data in production
    recommendations = hybrid_recommendations(user_id, query)

    print("\nRecommended Videos:")
    for rec in recommendations:
        print(f"Title: {rec['title']}\nVideo ID: {rec['video_id']}\nDescription: {rec['description']}\n")

# Run the main function
main()
