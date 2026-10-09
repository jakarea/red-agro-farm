with open("faq.html", "r") as f:
    content = f.read()

# Replace padding
new_content = content.replace("px-5 pb-5 md:px-6 md:pb-6", "px-5 pb-7 md:px-6 md:pb-8")

with open("faq.html", "w") as f:
    f.write(new_content)
