import openai
import os
API_KEY = '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'

os.environ['OPENAI_Key'] = API_KEY
openai.api_key = os.environ['OPENAI_Key']


def get_response(x):
    keep_prompting = True
    while keep_prompting:
        prompt = x
        if prompt == 'exit':
            keep_prompting = False
        else:
            response = openai.Completion.create(
                engine='text-davinci-003', prompt=prompt, max_tokens=200)

            ping = response['choices'][0]['text']
            print(response['choices'][0]['text'])
            return ping

    return "nope"


get_response("height of taj mahal")
