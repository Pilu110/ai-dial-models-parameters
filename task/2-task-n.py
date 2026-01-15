from task.app.main import run

# TODO:
#  Try the `n` parameter with different models (`deployment_name`). With the parameter `n`, we can configure how many
#       chat completion choices to generate for each input message
#  User massage: Why is the snow white?

# Models to try:
# - gpt-4o
# - claude-3-7-sonnet@20250219
# - gemini-2.5-pro

user_messages = ['Why is the snow white?', 'exit']
deployment_names = ['gpt-4o', 'claude-3-7-sonnet@20250219', 'gemini-2.5-pro']

for deployment_name in deployment_names:
    print(f"Running with {deployment_name} deployment...")
    try:
        run(
            deployment_name=deployment_name,
            print_request=True, # Switch to False if you do not want to see the request in console
            print_only_content=True, # Switch to True if you want to see only content from response
            user_messages=user_messages,
            n = 3
        )
    except Exception as ex:
        print(f"Deployment '{deployment_name}' failed with {ex}.")

# Pay attention to the number of choices in the response!
# If you have worked with ChatGPT, you have probably seen responses where ChatGPT offers you a choice between two
# responses to select which one you prefer. This is done with the `n` parameter.
