from task.app.main import run

# TODO:
#  Try `stop` parameter.
#  `stop` (str or list[str]): Tells the AI to stop generating text when it encounters specific words or phrases.
#  Like setting custom "end of response" triggers.
#       Default: None
#  User massage: Explain the key components of a Large Language Model architecture

user_messages = ["Explain the key components of a Large Language Model architecture", 'exit']
deployment_names = ['gpt-4o', 'claude-sonnet-4-5@20250929', 'gemini-2.5-pro']

for deployment_name in deployment_names:
    for stop in [["\n\n"], ["**Embedding Layer**", "**Transformer Blocks**", "**Training**"]]:
        print(f"Running with {deployment_name} deployment with stop {stop}...")
        try:
            run(
                deployment_name=deployment_name,
                print_request=False, # Switch to False if you do not want to see the request in console
                print_only_content=False, # Switch to True if you want to see only content from response
                user_messages=user_messages,
                stop = stop
            )
        except Exception as ex:
            print(f"Deployment '{deployment_name}' failed with {ex}.")

# With `stop` parameter we can stop content generation. It can be used for some policies/guardrails. For instance,
# we are the company with the name `Pear` and we don't want that anybody will see in results that our competitor `Apple`
# is cool (stop: ["Apple is cool", "Apple top"]).
# The `finish_reason` will be set as `stop`. So, the users won't know what is the real reason why LLM has stopped generation.