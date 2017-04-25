import requests
from bs4 import BeautifulSoup
import bs4 as bs
 
request = requests.get("https://www.amazon.com/gp/product/B00IOY8XWQ/ref=s9_acss_bw_cg_odseac_3c1_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-2&pf_rd_r=1M1XPKM973BPHNHM4W62&pf_rd_t=101&pf_rd_p=efc7ffcc-ed0d-49d5-bfa0-c646c006005f&pf_rd_i=6669702011")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", { "id": "priceblock_ourprice", "class": "a-size-medium a-color-price"})
string_price = element.text.strip()
 
price_without_symbol = string_price[4:]
 
price = float(price_without_symbol)
 
if price < 2000000:
        print("You should buy the chair!")
        print("The current price is  {}.".format(string_price))
else:
        print("Do not buy this!!")
 
# <span class="notranslate" id="prcIsum" itemprop="price" style="" content="39.99">US $39.99</span>
 
print(request.content)

'''<div class=><!-- react-text: 5589 -->₹<!-- /react-text --><!-- react-text: 5590 -->24,990<!-- /react-text --></div>  , "class": "notranslate"'''