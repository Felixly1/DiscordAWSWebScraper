from bs4 import BeautifulSoup
import requests

#Script to find the location of availability given a URL

def getParsedLocations(doc) -> list:
    '''
    Given a html parsed document 
    Returns lists of sublists on every Canada Computers store in ON 
    where each sublists contains info on location, stock, and address
    '''
    storesInOntario = doc.find_all(id="collapseON")
    storeInfoStrings = storesInOntario[0].stripped_strings
    uselessInfo = ["Set Preferred Store","Preferred Store","Today","Tomorrow","-"]
    allLocations = []
    parsedLocations = [] #2d array consisting of sublists of info about CC stores with GPU  
    #[0] = location, [1] = stock, [2] = address
    
    #Convert generated object into list   
    for string in storeInfoStrings:
        if (string not in uselessInfo):
            allLocations.append(string)

    #parse list into sublist     
    for i in range(0,len(allLocations), 3):
        sublist = allLocations[i:i+3]
        parsedLocations.append(sublist)
        
    return parsedLocations


def displayLocation(location) -> str:
    '''
    Given a location info as 3 elements, return its info
    '''
    
    str="Location: " + location[0] + "\nIn Stock: " + location[1] + "\nAddress: " + location[2] + "\n\n"
    return str
    

def displayInStock(parsedLocations) -> str:
    '''
    Given a list of parsed locations
    Returns the ones in stock in a compiled String
    '''
    str = ""
    for location in parsedLocations:
        if (location[1] != '0'):
            str += displayLocation(location)
    
    if (str):
        return str
    return None
        

def getInStockON(URL) -> None|str:
    '''
    Given a URL to a Canada Computers product
    Returns None if product not in stock
    Else return string of info
    '''
    results = requests.get(URL)
    doc = BeautifulSoup(results.text,"html.parser")
    locations = getParsedLocations(doc)
    output = displayInStock(locations)
    return output
        





