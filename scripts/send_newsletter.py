import os
import sys
import resend
import markdown2

resend.api_key = os.environ["RESEND_API_KEY"]

# Get input filename
filename = sys.argv[1] if len(sys.argv) > 1 else "newsletter.md"

# Load and convert
with open(filename, "r") as file:
    markdown_text = file.read()

html_content = markdown2.markdown(markdown_text)

params = {
    "from": "Ethereum Weekly <Week-In-Ethereum@wie.ercref.org>",
    "to": [os.environ["NEWSLETTER_RECIPIENT"]],
    "subject": "🚀 Weekly Ethereum Newsletter",
    "html": html_content,
}

res = resend.Emails.send(params)
print("✅ Newsletter sent! Response:", res)
