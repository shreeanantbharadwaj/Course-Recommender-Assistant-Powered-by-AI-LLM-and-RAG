import os
import openai
import pinecone

# Set your environment variables or replace these with your actual API keys
OPENAI_API_KEY="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"
PINECONE_API_KEY = "pcsk_5rmrx1_MguMuS9p76UXDS5Djoq9mcLafUsgA2AmJaL1dm38VXdN4UNMNmmwZwaSECxV9fi"
PINECONE_ENV = "us-east-1"  # You can change it according to your environment

# Initialize OpenAI API
def test_openai_connection():
    try:
        openai.api_key = OPENAI_API_KEY
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Or gpt-4 if you want
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Hello!"}
            ]
        )
        print("OpenAI API Connection Successful!")
        print("Response: ", response.choices[0].message["content"])
    except Exception as e:
        print(f"Error with OpenAI API: {e}")

# Initialize Pinecone API
# Initialize Pinecone API
def test_pinecone_connection():
    try:
        # Correctly instantiate the Pinecone client
        pc = pinecone.Pinecone(api_key=PINECONE_API_KEY)

        # Test if the connection is successful by listing available indexes
        indexes = pc.list_indexes()
        if indexes:
            print("Pinecone Connection Successful!")
            print("Available Indexes: ", indexes)
        else:
            print("No Pinecone indexes available.")
    except Exception as e:
        print(f"Error with Pinecone connection: {e}")

if __name__ == "__main__":
    test_openai_connection()
    test_pinecone_connection()
