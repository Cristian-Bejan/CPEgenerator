# CPEgenerator
A Python script that helps you generate CPE URIs based on the v2.3 CPE standard. This is particularly useful for bulk processing of products from the same vendor.

## Requirements
The script uses the `pyperclip` package to interact with the clipboard. Install it using pip:
```bash pip install pyperclip```

You can find more about pyperclip here: `pyperclip` on PyPI - https://pypi.org/project/pyperclip/

# Usage
1. Copy your list of product names to the clipboard. The script will automatically fetch these names when executed.
2. Run the script and follow the prompts:
  Vendor Name: Enter the vendor name as a single word (e.g., examplevendor).
  CPE Type: Choose the type of product:
    a for application
    o for operating system or firmware
    h for hardware
3. Output: The script will generate CPE URIs based on the input and copy them to your clipboard.

# Customization
Product Name Separator
By default, the script expects product names to be separated by a comma followed by a space (, ). If your product names are separated differently (e.g., by just a comma, a slash, etc.), you can easily adjust the separator in the code:
```products = get_unique_products(separator=", ")```

# Handling Special Characters
The script handles special characters in product names according to the CPE standard. You can further customize this by modifying the `process_special_chars` function.

# Example Workflow
1. Copy the following to your clipboard:
```product1, product2, product3```
2. Run the script:
```python cpegenerator.py```
3. Follow the prompts to enter the vendor name and select the product type.
4. Paste the generated CPE URIs from your clipboard into your desired location.

# Notes
The script automatically removes duplicate product names.
The base CPE URI (e.g., cpe:/a:examplevendor:) is constructed based on your input but will not appear in the final output.
If you encounter any issues or have feature requests, feel free to contribute to the repository or open an issue.

**Please do not pull requests for security issues. This project was intended to be used as a standalone script**
