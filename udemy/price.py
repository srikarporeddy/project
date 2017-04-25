import requests
from bs4 import BeautifulSoup
request = requests.get("https://www.amazon.com/gp/product/B00IOY8XWQ/ref=s9_acss_bw_cg_odseac_3c1_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-2&pf_rd_r=1M1XPKM973BPHNHM4W62&pf_rd_t=101&pf_rd_p=efc7ffcc-ed0d-49d5-bfa0-c646c006005f&pf_rd_i=6669702011")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", { "id": "priceblock_ourprice", "class": "a-size-medium a-color-price"})
string_price = element.text.strip()
int_price = (string_price[1:])
print(int_price, type(int_price))