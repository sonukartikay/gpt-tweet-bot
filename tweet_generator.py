import openai
import datetime

openai.api_key = "import os
openai.api_key = os.environ["OPENAI_API_KEY"]
"

now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
prompt = f"Write a short, witty tweet about a trending tech topic. Include the current date and time: {now}"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}],
    max_tokens=60
)

tweet = response['choices'][0]['message']['content'].strip()

with open("latest_tweet.txt", "w") as f:
    f.write(tweet)
print("Generated Tweet:", tweet)
