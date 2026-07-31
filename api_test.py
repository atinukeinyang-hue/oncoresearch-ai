import anthropic

# ==========================================
# PASTE YOUR NEW API KEY BELOW
# ==========================================

key = "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"

# ==========================================

print("=" * 50)
print("Testing Anthropic API Key...")
print("=" * 50)

print("Length of key:", len(key))
print("Starts with:", key[:13])
print()

client = anthropic.Anthropic(
    api_key=key
)

try:
    response = client.messages.create(
        model="claude-sonnet-5",
        max_tokens=20,
        thinking={"type": "disabled"},
        messages=[
            {
                "role": "user",
                "content": "Say hello in one sentence."
            }
        ]
    )

    print("✅ SUCCESS!")
    print()
    print("Claude replied:")
    print(response.content[0].text)

except Exception as e:
    print("❌ FAILED")
    print()
    print(type(e).__name__)
    print(e)