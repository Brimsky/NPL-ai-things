text = "@John: Šis ir lielisks produkts!!! Vai ne? 👏👏👏 http://example.com"

new_text = text.replace("@", "").replace("!!!", "").replace("👏👏👏", "").replace("http://example.com", "").lower()
print(new_text)