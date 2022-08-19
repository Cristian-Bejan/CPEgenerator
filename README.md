# CPEgenerator
A short script that will help you create CPE URIs based on the v2.3 CPE standard. Useful for bulk products that have the same vendor.

It uses the pyperclip package ```pip install pyperclip``` - https://pypi.org/project/pyperclip/
Comma is used as a separator for products. Easily change this ```products = pyperclip.paste().split(", ")```
