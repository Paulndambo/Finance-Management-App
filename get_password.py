import base64

timestamp = "20230311023439"
shortcode = "174379"
passkey = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"

# Concatenate the shortcode, passkey, and timestamp strings
data = f"{shortcode}{passkey}{timestamp}"

# Encode the data string to base64
encoded_data = base64.b64encode(data.encode())

# print(encoded_data.decode())  # Print the base64-encoded data as a string

a = "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMjMwMzExMDIzNDM5"
b = "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMjMwMzExMDIzNDM5"

print(a == b)
