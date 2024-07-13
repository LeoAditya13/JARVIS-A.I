import os
import openai

openai.api_key = "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"

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Write a Letter For an Salary Increment to My Boss \n",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)
