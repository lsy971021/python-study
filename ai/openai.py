import openai
import requests
import os


# def answer():
#     openai.api_key = "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"
#     prompt = """
#     你是谁
#         """
#     # completion = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=1024, n=1, temperature=0.5)
#     completion = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[{"role": "user", "content": prompt}]
#     )
#
#     result = completion["choices"][0]['message']['content'].strip()
#     print(result)
# answer()


def myimg(self):
    openai.api_key = "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"
    response = openai.Image.create(
        prompt="傍晚一个美女在海边的礁石上吹风，有夕阳和海鸥，沙滩上有小朋友在玩耍",
        n=2,
        size="1024x1024"
    )

    print(response)
    image_url = response['data'][0]['url']
    print(image_url)


# myimg()

def list():
    openai.api_key = os.getenv("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")

    completion = openai.ChatCompletion.create(
        model="text-davinci-003",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello!"}
        ]
    )

    print(completion.choices[0].message)


def xxx():
    a = 'sss'


list()
