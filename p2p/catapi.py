
import webbrowser, json, requests
class CatAPI:

    """Interface with the Cat API"""
    api_key = "live_pGPtu252IVJfrslX8KvUkqhFOmid15pf8qL7r2PqXiPlnEwYzg7JWGC2MZdwTW4u"

def main():
    print(get_img())
def get_img():
    url = "https://api.thecatapi.com/v1/images/search?api_key=live_pGPtu252IVJfrslX8KvUkqhFOmid15pf8qL7r2PqXiPlnEwYzg7JWGC2MZdwTW4u"
    myfile = requests.get(url)
    file = open('cat_data.json', 'wb')
    file.write(myfile.content)    
    file.close()

    file = open ('cat_data.json', "r")
    # https://www.geeksforgeeks.org/read-json-file-using-python/
    data = json.loads(file.read())  
    file.close()
    cat_url = data[0].get("url")
    webbrowser.open(cat_url)
    message = "Your image has been sent! Open your browser or click the link here: " + url
    return message


if __name__ == "__main__":
    main()







    
