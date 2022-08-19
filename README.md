# CPEgenerator
A short script that will help you create CPE URIs based on the v2.3 CPE standard. Useful for bulk products that have the same vendor.

It uses the pyperclip package:  
```pip install pyperclip```  
https://pypi.org/project/pyperclip/

Comma is used as a separator for products. Easily change this in the following line of code:  
```products = pyperclip.paste().split(", ")```

**Please do not pull requests for security issues. This project was intended to be used as a standalone script**
