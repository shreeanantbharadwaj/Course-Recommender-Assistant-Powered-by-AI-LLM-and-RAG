import openai

# Set your OpenAI API key directly for testing
openai.api_key = "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"

# Check if the API key is set
if not openai.api_key:
    raise RuntimeError("OpenAI API key is not set.")

try:
    # Test the OpenAI API by generating an embedding
    response = openai.Embedding.create(
        model="text-embedding-ada-002",
        input="Test query"
    )
    print("Embedding generated successfully:")
    print(response)
except openai.error.AuthenticationError:
    print("Authentication failed. Please check your API key.")
except Exception as e:
    print("An error occurred:", e)
