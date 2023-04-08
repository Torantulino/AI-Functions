import openai

def ai_function(function, args, description, model = "gpt-4"):
    # parse args to comma separated string
    args = ", ".join(args)
    messages = [{"role": "system", "content": f"You are now the following python function: ```# {description}\n{function}```\n\nOnly respond with your `return` value. no verbose, no chat."},{"role": "user", "content": args}]

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0
    )

    return response.choices[0].message["content"]
