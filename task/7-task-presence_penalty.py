from task.app.main import run

# TODO:
#  Try `presence_penalty` parameter.
#  Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's
#  likelihood to talk about new topics. Higher values == more topic diversity.
#       Range: -2.0 to 2.0
#       Default: 0.0
#  User massage: What is an entropy in LLM's responses?

user_messages = ["What is an entropy in LLM's responses?", 'exit']

for presence_penalty in range(-2, 3):
    print(f"Running with {presence_penalty} presence_penalty...")
    run(
        deployment_name='gpt-4o',
        print_request=False, # Switch to False if you do not want to see the request in console
        print_only_content=True, # Switch to True if you want to see only content from response
        user_messages=user_messages,
        presence_penalty=presence_penalty,
        max_tokens=200,
    )

# In the final result, we can see that the higher `presence_penalty` (2.0) the more LLM is trying to add topics that
# somehow related to the main topic.
# For Anthropic and Gemini this parameter will be ignored