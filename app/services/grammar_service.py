import re

def find_repeated_words(text: str):
    issues = []
    pattern = r"\b(\w+)\s+\1\b"
    matches = re.findall(pattern, text, flags=re.IGNORECASE)

    for word in matches:
        issues.append(f"Repeated word found: '{word}'")

    return list(set(issues))