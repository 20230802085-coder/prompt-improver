from openai import OpenAI
import boto3


client = OpenAI(api_key="sk-proj-1lxG------")

user_prompt = input("Enter your prompt: ")

improved_prompt = "Generate a clear, detailed and well-structured response for: " + user_prompt + ". "

if "project" in user_prompt:
    improved_prompt += "Include real-world applications and practical examples. "

if "python" in user_prompt:
    improved_prompt += "Focus specifically on Python implementation. "

if "code" in user_prompt:
    improved_prompt += "Provide clean and well-commented code with explanation. "

if "ideas" in user_prompt:
    improved_prompt += "List multiple creative and unique ideas. "

if "learn" in user_prompt:
    improved_prompt += "Explain step-by-step in a simple manner. "

if "beginner" in user_prompt:
    improved_prompt += "Keep it beginner-friendly. "

if "advanced" in user_prompt:
    improved_prompt += "Also include some advanced concepts. "

if "example" in user_prompt:
    improved_prompt += "Give proper examples for better understanding. "

if "explain" in user_prompt:
    improved_prompt += "Explain clearly in simple language. "

print("\nYour Improved Prompt (Before AI):")
print(improved_prompt)

# --------- AI PART ---------
try:
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": improved_prompt}
        ]
    )

    final_output = response.choices[0].message.content

    print("\nFinal Improved Prompt:")
    print(final_output)

except Exception as e:
    print("\nAI not working, showing logic-based prompt instead.\n")
    final_output = improved_prompt
    print(final_output)

with open("output.txt", "w") as f:
    f.write("User Prompt:\n" + user_prompt + "\n\n")
    f.write("Improved Prompt:\n" + improved_prompt + "\n\n")
    f.write("Final Output:\n" + final_output)

print("\nOutput saved to file.")


aws_access_key = "AKIA5KZ------"
aws_secret_key = "zryxHJ1------"

try:
    s3 = boto3.client(
        's3',
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_key,
        region_name='ap-south-1'
    )

    bucket_name = "prompt-improver-data"

    s3.upload_file("output.txt", bucket_name, "output.txt")

    print("File uploaded to S3 successfully.")

except Exception as e:
    print("S3 upload failed. Check your AWS credentials.")