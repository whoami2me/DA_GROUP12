import requests

url = input("Please enter url:")
req = requests.get(url)

print("Status code:")
print("\t *", req.status_code)

header = requests.head(url)
print("Header:")
print("**********")

for line in header.headers:
    print("\t", line, ":", head.headers[line])
print("**********")

headers = {
    'User-Agent' : 'Mobile'
}

url2 = input("Please enter url2:")
modified_ua = requests.get(url2, headers=headers)
print(modified_ua.text)

print("end of part 5 \n**************************")

class NewSpider(scrapy.Spider):
 name = "new spider"
 start_urls = ["https://www.ite.edu.sg"]
 def parse(self,response):
  css_selector = 'img'
  for x in response.css(css_selector):
   newsel = '@src'
   yield{
    'Image Link' : x.xpath(newsel).extract_first(),
   }
   Page_selector = '.next a ::attr(href)'
   next_page = response.css(Page_selector).extract_first()
   if next_page:
    yield scrapy.Request(
      response.urljoin(next_page),
      callback=self.parse
    )
    
#missing 6ii , 6iii and 8 
