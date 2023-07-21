def dalle(message):
    import requests
    import openai

    # Set up the OpenAI API client
    openai.api_key = "your-api-key"

    # Set up the model and prompt
    model_engine = "text-davinci-003"
    prompt = message

    # Generate a response
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    response = requests.get(image_url)
    with open("image.jpg", "wb") as f:
        f.write(response.content)

    print(image_url)


dalle(input("Enter something : "))
