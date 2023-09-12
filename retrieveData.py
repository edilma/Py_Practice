import urllib.request
''' With this library we can go to any website and read the data '''

def main():
    myUrl = "http://www.google.com"
    #myUrl = "https://dedeudas.com/programa-del-bank-of-america-para-comprar-casa-que-es-para-quien-es-y-como-acceder-a-el/"
    weburl = urllib.request.urlopen(myUrl) #returns a webresponse object
    print("result code: ", weburl.getcode())
    data = weburl.read()
    print (data)


if __name__ =="__main__":
    main()