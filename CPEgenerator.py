import pyperclip
import urllib.parse

def get_unique_products(separator=", "):
    """Fetch and split the copied product names from clipboard, then remove duplicates."""
    products = pyperclip.paste().split(separator)
    return list(dict.fromkeys(products))

def get_vendor_name():
    """Prompt user for a valid vendor name (single word)."""
    attempts = 0
    while True:
        vendor = input("Enter just the vendor name (one word): ").strip().lower()
        if len(vendor.split()) == 1:
            return vendor
        attempts += 1
        if attempts >= 3:
            print("Please focus and use only one word for the vendor, e.g., very_cool_vendor_name or very-cool-vendor-name")
        if attempts >= 4:
            exit("Take a break and try again later.")

def get_cpe_type():
    """Prompt user for a valid CPE type (a, o, h)."""
    attempts = 0
    while True:
        cpe_type = input("Enter the product type (a for application, o for OS, h for hardware): ").strip().lower()
        if cpe_type in {"a", "o", "h"}:
            return cpe_type
        attempts += 1
        if attempts >= 3:
            print("Focus - only enter 'a', 'o', or 'h' for your product type.")
        if attempts >= 4:
            exit("Take a break and try again later.")

def process_special_chars(product_name):
    """Encode the product name and handle special characters."""
    special_chars = {'_': '%5f', '.': '%2e', '-': '%2d', '~': '%7e'}
    product_name = urllib.parse.quote(product_name, safe=' ')
    return product_name.translate(str.maketrans(special_chars))

def build_cpe_uri(base_cpe, product_name, is_os=False):
    """Build the CPE URI from the base CPE and product name."""
    processed_name = process_special_chars(product_name)
    cpe_uri = base_cpe + processed_name.replace(' ', '_')
    if is_os:
        cpe_uri += "_firmware"
    return cpe_uri

def generate_cpe_uris(cpe_type, vendor, products):
    """Generate CPE URIs based on the type and vendor."""
    base_cpe = f"cpe:/{cpe_type}:{vendor}:"
    output = ""

    if cpe_type == "a":
        output = "\n".join(build_cpe_uri(base_cpe, product) for product in products)
    elif cpe_type in {"h", "o"}:
        output_hardware = "\n".join(build_cpe_uri(f"cpe:/h:{vendor}:", product) for product in products)
        output_os = "\n".join(build_cpe_uri(f"cpe:/o:{vendor}:", product, is_os=True) for product in products)
        output = output_hardware + "\n" + output_os

    return output

def main():
    products = get_unique_products()
    vendor = get_vendor_name()
    cpe_type = get_cpe_type()
    output = generate_cpe_uris(cpe_type, vendor, products)
    pyperclip.copy(output)
    print("\nGenerated CPE URIs:\n")
    print(output)

if __name__ == "__main__":
    main()
