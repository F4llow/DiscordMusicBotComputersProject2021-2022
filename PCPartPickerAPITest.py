#installed pcpartpicker which is an unofficial api for pcpartpicker
#after further research it seems limited in the information that i can obtain
#installed a second unofficial api known as pcpartscraper
#this seems like a better fit for what i will be doing
#lets see how this goes mr jeet chugh
#after testing this second one something is going wrong
#tbh i might hav done something wrong but im almost certain that its on their end
#it is relatively old but idk man
#next test
#this one is called pypartpicker
#again, unofficial, all that gud stuff
#wow
#wat do uk
#this random one worked
#thx mr quake
#guess i wont hav to use the fourth option
#time to take this to the next step
#cya cya

#for someone using this make sure you type this into your terminal once you
#are in the correct folder in your terminal
#pip install pypartpicker

#you know the drill
from pypartpicker import Scraper

#now u dont hav to write it out the entire time
sc = Scraper()

#for practice i will be testing each of the non async methods
#idk the difference but ik that the methods are not backwards compatible
#for example my discord bot uses async everything while this does not
#they are almost identical except for adding await before each time sc is called

#part_search() test
#also converts the list to string then gets rid of brackets for easy compatibility
query = "i9"
search = sc.part_search(query, limit = 1, region = "us")
search = str(search)
search = search[1:-1]
#print(search)

#fetch_product() test
link = "https://pcpartpicker.com/product/mDcG3C/intel-core-i9-11900k-35-ghz-8-core-processor-bx8070811900k"
var = sc.fetch_product(link)
#print(var)

#fetch_list(test)
list = "https://pcpartpicker.com/list/Tzx22V"
var2 = sc.fetch_list(list)
#print(var2)

#unable to get the other methods that he uses working
#this should not be a problem as they are kind of useless lol
#these methods can be combined into mor complex ones such as the following

#test function that prints the name of the first search result from your search query
#keep in mind that it returns an error if there is no result, or if there is no price
def nameAndPrice():
    query1 = input("Please enter your PCPartPicker search: ")
    result = sc.part_search(query1, limit = 1, region = "us")
    firstProductName = result[0].name
    firstProductPrice = result[0].price
    print("The " + firstProductName + " is " + firstProductPrice)

#nameAndPrice()

def pcpartpicker():
    query2 = input("Please enter your PCPartPicker search: ")
    result2 = sc.part_search(query2, limit = 1, region = "us")
    firstProductName = result2[0].name
    firstProductPrice = result2[0].price
    firstProductType = result2[0].type
    firstProductUrl = result2[0].url
    firstProductImage = result2[0].image
    print(firstProductName)
    print(firstProductPrice)
    print(firstProductType)
    print(firstProductUrl)
    print(firstProductImage)

pcpartpicker()
