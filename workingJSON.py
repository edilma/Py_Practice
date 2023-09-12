import urllib.request
import json

def printResults(data):
    #use the json module to load the string data into a dictionary
    theJSON = json.loads(data)

    #Access the content of the json like any other object
    if "title" in theJSON["metadata"]:
        print (theJSON["metadata"]["title"])
    # print the count of earthquakes
    count = theJSON["metadata"]["count"]
    print (count, "events recorded")

    #print some information from the data
    for i in theJSON["features"]:
        print (i["properties"]["place"])
    print ("--------------------------------------\n")

    #print the earthquakes that are stronger than 4
    for i in theJSON["features"]:
        if i["properties"]["mag"] >= 4.0:
            print(i["properties"]["place"])
    print ("--------------------------------------\n")

    #print events where at least 1 person reported feeling something
    print("\nEvents that were felt: ") 
    for i in theJSON["features"]:
        feltReports = i["properties"]["felt"]
        if feltReports != None:
            if feltReports > 0:
                print (i["properties"]["place"], feltReports, " times") 



def main():
    #the data feed
    urlData = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_week.geojson"

    weburl = urllib.request.urlopen(urlData)
    print("result code: ", weburl.getcode())
    if weburl.getcode() ==200:
        data = weburl.read()
        printResults (data)
    else :
        print("Received an error from the server, cannot print results ", weburl.getcode())

if __name__ =="__main__":
    main()

