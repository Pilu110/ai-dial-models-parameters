from task.app.main import run

# TODO:
#  Try the `temperature` parameter that controls the randomness of the output. It's a parameter for balancing creativity
#        and determinism. Range: 0.0 to 2.0, Default: 1.0
#  User massage: Describe the sound that the color purple makes when it's angry

user_messages = ["Describe the sound that the color purple makes when it's angry", 'exit']
deployment_names = ['gpt-4o', 'claude-sonnet-4-5@20250929', 'gemini-2.5-pro']

for deployment_name in deployment_names:
    for temperature in [0.0, 0.5, 1.0, 1.5, 2.0, 2.1]:
        print(f"Running with {deployment_name} deployment with temperature {temperature}...")
        try:
            run(
                deployment_name=deployment_name,
                print_request=False, # Switch to False if you do not want to see the request in console
                print_only_content=True, # Switch to True if you want to see only content from response
                user_messages=user_messages,
                temperature = temperature
            )
        except Exception as ex:
            print(f"Deployment '{deployment_name}' failed with {ex}.")
