import re

with open('products.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Make image bigger
content = content.replace('w-40 sm:w-52', 'w-48 sm:w-64 md:w-72')

def process_product(block):
    # find the details link to get the product ID
    url_match = re.search(r'href="(product\.html\?id=[^"]+)"[^>]*>বিস্তারিত দেখুন', block)
    if not url_match:
        return block
    url = url_match.group(1)
    
    # Replace image div with a tag
    block = re.sub(
        r'<div (class="w-48 sm:w-64 md:w-72 flex-shrink-0 bg-cover[^"]*" style="[^"]*")>',
        f'<a href="{url}" \\1 block>',
        block
    )
    
    # We also need to change the closing </div> of that image container to </a>
    block = block.replace('          </div>\n          <div class="flex-1 p-5', '          </a>\n          <div class="flex-1 p-5')
    
    # Wrap title in <a>
    block = re.sub(
        r'(<h3 class="font-bold text-gray-900 text-base[^>]*>.*?</h3>)',
        f'<a href="{url}" class="hover:text-primary-600 transition-colors">\\1</a>',
        block
    )
    
    return block

parts = content.split('class="product-item ')
new_parts = [parts[0]]
for part in parts[1:]:
    full_part = 'class="product-item ' + part
    if 'data-category=' in full_part and 'id=' in full_part:
        full_part = process_product(full_part)
    new_parts.append(full_part)

new_content = "".join(new_parts)

with open('products.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done")
