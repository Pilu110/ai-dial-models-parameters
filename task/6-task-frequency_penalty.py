from task.app.main import run

# TODO:
#  Try `frequency_penalty` parameter.
#  Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's
#  likelihood to repeat the same line verbatim. Higher values == less repetitive text.
#       Range: -2.0 to 2.0
#       Default: 0.0
#  User massage: Explain the water cycle in simple terms for children

user_messages = ["Explain the water cycle in simple terms for children", 'exit']

for frequency_penalty in range(-2, 3):
    print(f"Running with {frequency_penalty} frequency_penalty...")
    run(
        deployment_name='gpt-4o',
        print_request=False, # Switch to False if you do not want to see the request in console
        print_only_content=True, # Switch to True if you want to see only content from response
        user_messages=user_messages,
        frequency_penalty=frequency_penalty,
        max_tokens=200,
    )
# Pay attention that when we set for `gpt-4o` frequency_penalty as -2.0 - the request is running too long,
# and in the result we can get something strange (such as repetitive words in the end).
# Copy the results and then check with separate request and ask LLM where is more repetitive blocks in texts.
# For Anthropic and Gemini this parameter will be ignored