import pandas as pd
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob
from colorama import Fore, Style, init

init(autoreset=True)

try:
    df = pd.read_csv("imdb_top_1000.csv")
except FileNotFoundError:
    print(Fore.RED + "Dataset file not found. Please place imdb_top_1000.csv in the working directory.")
    exit()

df['Overview'] = df['Overview'].fillna("")
df['Genre'] = df['Genre'].fillna("")
df['combined_features'] = df['Genre'] + " " + df['Overview']

vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['combined_features'])

similarity_matrix = cosine_similarity(tfidf_matrix)

def display_movie(index):
    print(Fore.CYAN + "\n🎬 Movie Details")
    print(Fore.YELLOW + "Title:", df.iloc[index]['Series_Title'])
    print(Fore.GREEN + "Genre:", df.iloc[index]['Genre'])
    print(Fore.MAGENTA + "IMDB Rating:", df.iloc[index]['IMDB_Rating'])

    overview = df.iloc[index]['Overview']
    sentiment = TextBlob(overview).sentiment.polarity

    print(Fore.WHITE + "Overview:", overview[:300] + "...")

    if sentiment > 0:
        print(Fore.GREEN + "Sentiment: Positive 😊")
    elif sentiment < 0:
        print(Fore.RED + "Sentiment: Negative 😢")
    else:
        print(Fore.YELLOW + "Sentiment: Neutral 😐")


def recommend(movie_title, num_recommendations=5):
    if movie_title not in df['Series_Title'].values:
        print(Fore.RED + "Movie not found in dataset.")
        return

    movie_index = df[df['Series_Title'] == movie_title].index[0]
    similarity_scores = list(enumerate(similarity_matrix[movie_index]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    print(Fore.BLUE + f"\nTop {num_recommendations} Recommendations for '{movie_title}':")

    count = 0
    for i in similarity_scores[1:]:
        print(Fore.WHITE + "-", df.iloc[i[0]]['Series_Title'])
        count += 1
        if count >= num_recommendations:
            break


def random_movie():
    index = random.randint(0, len(df) - 1)
    display_movie(index)


while True:
    print(Fore.CYAN + "\n=== 🎥 Movie Recommendation System ===")
    print("1. Get Random Movie")
    print("2. Get Recommendations by Title")
    print("3. Exit")

    choice = input(Fore.YELLOW + "Enter your choice: ")

    if choice == "1":
        random_movie()

    elif choice == "2":
        title = input(Fore.YELLOW + "Enter movie title exactly as in dataset: ")
        recommend(title)

    elif choice == "3":
        print(Fore.GREEN + "Goodbye! 🍿")
        break

    else:
        print(Fore.RED + "Invalid choice. Try again.")
