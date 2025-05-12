import ollama
import json

import ollama
import json
import pprint

# Generating RAG response with DeepSeek (Ollama)
def invoke_llama(prompt, matched_items):
    """
    Invoke the DeepSeek model (from Ollama).
    """

    # Define your system prompt(s).
    system_msg = [
        { "text": """You are a helpful assistant for question answering. 
                    The text context is relevant information retrieved. 
                    The provided image(s) are relevant information retrieved."""}
    ]

    # Define one or more messages using the "user" and "assistant" roles.
    message_content = []

    # Process the matched items (text or image)
    for item in matched_items:
        if item['type'] == 'text' or item['type'] == 'table':
            message_content.append({"text": item['text']})
        else:
            # Assuming the image is in the correct format
            message_content.append({"image": {
                                        "format": "png",
                                        "source": {"bytes": item['image']},
                                    }
                                })

    # Configure the inference parameters (this may need tweaking based on your use case)
    inf_params = {"max_new_tokens": 300, 
                  "top_p": 0.9, 
                  "top_k": 20}

    # Define the final message list
    message_list = [
        {"role": "user", "content": message_content}
    ]
    
    # Add the prompt to the message list
    message_list.append({"role": "user", "content": [{"text": prompt}]})

    # Prepare the request in the native format
    native_request = {
        "messages": message_list,
        "system": system_msg,
        "inferenceConfig": inf_params,
    }

    # Initialize the Ollama client (using DeepSeek as the model)
    model_id = "llama3.3:70b"# "deepseek-r1:1.5b" #"deepseek-r1:70b" 
    client = ollama.chat(model=model_id, messages=[{"role": "user", "content": json.dumps(native_request)}])

    # pprint.pprint(client)

    # Invoke the model and extract the response body
    # response = client['text']
    response = client.message["content"]
    return response

