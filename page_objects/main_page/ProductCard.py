from page_objects.BasePage import BasePage

featered_block = {"css": "#content"}
featered_block_title = {"css": featered_block['css'] + ' h3'}
featured_block_row = {"css": featered_block['css'] + ' .row'}
featured_block_element = {"css": featured_block_row['css'] + ' .product-layout'}
featured_block_element_image = {"css": featured_block_element["css"] + ' .image'}
featured_block_element_caption = {"css": featured_block_element["css"] + ' .caption'}
featured_block_element_caption_header = {"css": featured_block_element["css"] + ' h4'}
featured_block_element_caption_paragraph = {"css": featured_block_element["css"] + ' p'}

featured_block_element_caption_price = {"css": featured_block_element_caption["css"] + ' .price'}
featured_block_element_caption_price_tax = {"css": featured_block_element_caption_price["css"] + '-tax'}


class ProductCard(BasePage):
    def get_currency(self):
        price = self._get_element_text(featured_block_element_caption_price)
        if "$" in price:
            currency = '$'
        elif "€" in price:
            currency = '€'
        else:
            currency = '£'
        return currency
