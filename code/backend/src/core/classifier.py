import openai

# Example function using OpenAI for classification
def classify_request(email_body):
    prompt = f"Classify the following email content into a loan servicing request type and sub-type: {email_body}"
    
    response = openai.Completion.create(
        model="gpt-3.5-turbo",  # or the model of your choice
        prompt=prompt,
        max_tokens=100,
        temperature=0.2
    )
    
    return response.choices[0].text.strip()
