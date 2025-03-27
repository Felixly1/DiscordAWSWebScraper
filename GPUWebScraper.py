from bs4 import BeautifulSoup
import requests
import re
import GetProductAvailability

#Given a search url, list the first 12 products that show up
#Only 12 becasue of lazy loading


url = "https://www.canadacomputers.com/en/powered-by-intel/266476/asrock-intel-arc-b580-steel-legend-12gb-gddr6-oc-battlemage-gpu-b580-sl-12go.html"


def displayStockOfSearchResult(URL) -> str:
    '''
    Given a URL of a search in Canada Computers
    Return a string with the stock information of the first 12 items
    '''
    results = requests.get(URL)
    doc = BeautifulSoup(results.text,"html.parser")
    displayString = ""

    #List of all the graphics card with the URL search above
    products = doc.find_all(id=re.compile(r"product_card_\d+"))
    if products:
        for product in products:
            print(product)
            productTitle = product.find(class_=re.compile(r"product-title"))
            productLinkTag = productTitle.find("a")
            href = productLinkTag.get("href","")
            if (productString := GetProductAvailability.getInStockON(href)):   
                productString = GetProductAvailability.getInStockON(href) #Prints Product info   
                displayString += productLinkTag.text #Prints Name of Product
                displayString += "\n=====================================\n"
                displayString += productString 
                displayString += "\n"
            else:
                displayString += "None in Stock\n\n"
        return displayString
    else:
        return ("No Products Found with url: " + url)   
    
def checkIfInStock() -> None|str:
    '''
    Function specifically made for bot to run to find intel b580 stock 
    Returns product info if a item appears in stock after a search result, else None
    '''
    url = "https://www.canadacomputers.com/en/powered-by-intel/266476/asrock-intel-arc-b580-steel-legend-12gb-gddr6-oc-battlemage-gpu-b580-sl-12go.html"
    results = requests.get(url)
    doc = BeautifulSoup(results.text,"html.parser")
    
    #List of all the graphics card with the URL search above
    products = doc.find_all(id=re.compile(r"product_card_\d+"))
    productTitle = doc.find(class_=re.compile(r"product-title"))
    
    
    if products:
        for product in products:
            productTitle = product.find(class_=re.compile(r"product-title"))
            productLinkTag = productTitle.find("a")
            href = productLinkTag.get("href","")
            if (output:= GetProductAvailability.getInStockON(href)):
                return output     
    return None