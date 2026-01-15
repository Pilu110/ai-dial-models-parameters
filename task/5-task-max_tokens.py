from task.app.main import run

# TODO:
#  Try `max_tokens` parameter. It sets the maximum length of the AI's response. The AI will stop generating text once it hits this limit.
#  User massage: What is token when we are working with LLM?

user_messages = ["What is token when we are working with LLM?", 'exit']
deployment_names = ['gpt-4o', 'claude-sonnet-4-5@20250929', 'gemini-2.5-pro']

for deployment_name in deployment_names:
    for max_tokens in [5, 10, 20]:
        print(f"Running with {deployment_name} deployment with max_tokens {max_tokens}...")
        try:
            run(
                deployment_name=deployment_name,
                print_request=False, # Switch to False if you do not want to see the request in console
                print_only_content=False, # Switch to True if you want to see only content from response
                user_messages=user_messages,
                max_tokens = max_tokens
            )
        except Exception as ex:
            print(f"Deployment '{deployment_name}' failed with {ex}.")


# Previously, we have seen that the `finish_reason` in choice was `stop`, but now it is `length`, and if you check the
# `content,` it is clearly unfinished.