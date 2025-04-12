import re

def is_html_balanced(html):
    tags = re.finditer(r'</?([a-zA-Z][a-zA-Z0-9]*)[^>]*>', html)
    stack = []

    for tag in tags:
        full_tag = tag.group(0)
        tag_name = tag.group(1)

        if full_tag.startswith('</'):
            if not stack or stack[-1] != tag_name:
                return False
            stack.pop()
        elif not full_tag.endswith('/>'):
            stack.append(tag_name)

    return len(stack) == 0

# Test cases
test_cases = {
    "Test 1 (Balanced)": "<div><p>Hello</p></div>",
    "Test 2 (Unbalanced)": "<div><p>Hello</div></p>",
    "Test 3 (Balanced with <br/>)": "<div><br/></div>",
    "Test 4 (Missing closing tag)": "<ul><li>Item 1<li>Item 2</ul>",
    "Test 5 (Self-closing <img>)": "<div><img src='photo.png' /></div>",
    "Test 6 (Wrong order)": "<b><i>Text</b></i>",
    "Test 7 (No tags)": "Text with no HTML",
    "Test 8 (Only self-closing tags)": "<hr/><br/><img/>",
    "Test 9 (Proper nesting)": "<section><article><h1>Title</h1></article></section>",
}

print("TEST RESULTS:\n")
for name, html in test_cases.items():
    result = is_html_balanced(html)
    status = "Balanced" if result else "Not Balanced"
    print(f"{name} → {status}")
