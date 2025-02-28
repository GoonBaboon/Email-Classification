import pandas as pd
import re

# Load the dataset
df = pd.read_csv('emails.csv')

def extract_email_body(message):
    """Remove headers and return only the email body."""
    match = re.split(r'\n\n+', message, maxsplit=1)  # Split at first empty line
    return match[1] if len(match) > 1 else message  # Return only the body

# Apply extraction to all messages
df["cleaned_message"] = df["message"].apply(extract_email_body)

# Show some cleaned messages
# print(df[["cleaned_message"]].head(5))
print(df.columns)
