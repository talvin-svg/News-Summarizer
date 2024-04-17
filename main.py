import openai
from dotenv import load_dotenv
import time
import logging
import os
import requests
import json

# from datetime import datetime


load_dotenv()

client = openai.OpenAI()
model = "gpt-3.5-turbo-16k"

news_api_key = os.environ.get("NEWS_API_KEY")


def get_news(topic):
    url = (
        f"https://newsapi.org/v2/everything?q={topic}&apiKey={news_api_key}&pageSize=5"
    )
    try:
        response = requests.get(url)
        if response.status_code == 200:
            news = json.dumps(response.json(), indent=4)
            news_json = json.loads(news)

            data = news_json

            # Access all the fields in the JSON response

            status = data["status"]
            totalResults = data["totalResults"]
            articles = data["articles"]
            final_news = []
            for article in articles:
                source_name = article["source"]["name"]
                author = article["author"]
                title = article["title"]
                description = article["description"]
                url = article["url"]
                urlToImage = article["urlToImage"]
                publishedAt = article["publishedAt"]
                content = article["content"]

                title_description = f"""
                    Title: {title},
                    Author: {author},
                    Source: {source_name},
                    Description: {description},
                    URL: {url}
 
                 """
            final_news.append(title_description)

            return final_news
        else:
            return []
    except requests.exceptions.RequestException as e:
        print("Error occured during API request", e)


def main():
    news = get_news("bitcoin")
    print(news)


if __name__ == "__main__":
    main()
