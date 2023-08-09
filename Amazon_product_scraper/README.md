# Amazon Product Scraper

## Description of package/script

Scrape the details of a product from Amazon using Python and Beautiful Soup.The details include

- Product Name
- Product Price
- Product Rating
- Product Image
- Customer Reviews

## Setup instructions

We will setup the environment and install the required packages and libraries using requirements.txt file. Run the following commands in the terminal to install the required packages and libraries.

```bash
pip install -r requirements.txt
```

"""
        Class - `Product`\n
        Example -\n
        ```python
        product = Product(product_name="watch")
        product.get_product()

```
        Return\n
        ```python
        return
        {
            "data": product_link,
            "message": f"Product data has been fetched",
        }
```

"""

## Modules used (available in requirements.txt)

- requests_html
- BeautifulSoup


### Developed by [Arvind Srivastav](https://github.com/alwenpy)
