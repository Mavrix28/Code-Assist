import requests
import json
import gradio as gr

url = "http://localhost:11434/api/generate"

headers = {
    "Content-Type": "application/json"
}

history = []

def generate_response(prompt):
    try:
        history.append(prompt)
        final_prompt = "\n".join(history)

        data = {
            "model": "CodeMate",
            "prompt": final_prompt,
            "stream": False,
        }
        response = requests.post(url, headers=headers, data=json.dumps(data), verify=False)

        if response.status_code == 200:
            response_data = response.json()  # Parses the response text as JSON
            actual_response = response_data.get('response', "No response key found in server response")
            return actual_response
        else:
            return f"Error {response.status_code}: {response.text}"
    except Exception as e:
        return f"An error occurred: {str(e)}"

interface = gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(label="Enter your prompt here", placeholder="Type here..."),
    outputs="text",
    title="Code with CodeMate",
    description="This is a CodeMate to help you in code . Ask anything!",
    theme="compact"  # You can choose from themes like "compact", "huggingface", etc.
)

interface.launch()