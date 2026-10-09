with open("faq.html", "r") as f:
    content = f.read()

# I will fix the regex. The previous python script used string replacement.
# Structure is:
# <div class="faq-answer">
#   <div class="px-5 pb-7 md:px-6 md:pb-8 text-gray-600 bangla leading-relaxed text-sm">
#      text...
#   </div>
# </div>

import re

# We want to change:
# <div class="px-5 pb-7 md:px-6 md:pb-8 text-gray-600 bangla leading-relaxed text-sm">
# to:
# <div><div class="px-5 pb-5 md:px-6 md:pb-6 text-gray-600 bangla leading-relaxed text-sm">
# and the closing </div> to </div></div>

# First, find all faq-answer blocks
def replace_answer(match):
    inner = match.group(1)
    # The inner div has class="px-5 pb-7..."
    # Replace the class
    inner = inner.replace("px-5 pb-7 md:px-6 md:pb-8", "px-5 pb-6 md:px-6 md:pb-7")
    return f'<div class="faq-answer">\n            <div>\n              {inner.strip()}\n            </div>\n          </div>'

new_content = re.sub(r'<div class="faq-answer">\s*<div class="px-5[^>]+>([\s\S]*?)</div>\s*</div>', 
                     lambda m: f'<div class="faq-answer">\n            <div>\n              <div class="px-5 pb-6 md:px-6 md:pb-7 text-gray-600 bangla leading-relaxed text-sm">\n                {m.group(1).strip()}\n              </div>\n            </div>\n          </div>', 
                     content)

with open("faq.html", "w") as f:
    f.write(new_content)
