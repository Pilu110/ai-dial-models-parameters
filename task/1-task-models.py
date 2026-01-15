from task.app.main import run

# HINT: All available models you can find here: https://ai-proxy.lab.epam.com/openai/models

# TODO:
#  Try different models (`deployment_name`) with such user request:
#  User message: What LLMs can do?

# Models to try:
# - gpt-4o
# - claude-3-7-sonnet@20250219
# - gemini-2.5-pro

user_messages = ['What LLMs can do?', 'exit']
deployment_names = ['gpt-4o', 'claude-3-7-sonnet@20250219', 'gemini-2.5-pro']

for deployment_name in deployment_names:
    print(f"Running with {deployment_name} deployment...")
    try:
        run(
            deployment_name=deployment_name,
            print_request=True, # Switch to False if you do not want to see the request in console
            print_only_content=True, # Switch to True if you want to see only content from response
            user_messages=user_messages
        )
    except Exception as ex:
        print(f"Deployment '{deployment_name}' failed with {ex}.")

# The main goal of this task is to explore the functional capabilities of DIAL to be able to work with different
# LLMs through unified API