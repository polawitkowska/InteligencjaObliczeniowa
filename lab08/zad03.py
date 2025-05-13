import requests
import json

def get_posts(subreddit, limit=100):
    url = f"https://www.reddit.com/r/{subreddit}/new.json?limit={limit}"

    try:
        response = requests.get(url=url)
        data = response.json()

        posts = []
        for post in data["data"]["children"]:
            post_data = post["data"]
            posts.append({
                'title': post_data['title'],
                'author': post_data['author'],
                'score': post_data['score'],
                'text': post_data['selftext']
            })

        with open(f'{subreddit}_posts.json', 'w', encoding='utf-8') as f:
            json.dump(posts, f, indent=2, ensure_ascii=False)
            
        return posts
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return

posts = get_posts("BeginnerWoodWorking")
if posts:
    print(f"Got {len(posts)} posts")

    for post in posts[:5]:
        print(f"\nTitle: {post['title']}")
        print(f"Author: {post['author']}")
        print(f"Text: {post['text']}")
