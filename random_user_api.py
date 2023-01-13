# import request that HTTP our requests
import requests

# create a loop to get 10request only

for i in range(10):

  # get male requsets only 

    gender = '?gender=male'

  # use request to access the API and read as json
    response = requests.get("https://randomuser.me/api/" + gender)
    data = response.json()

    data = data["results"]

    data = data[0]

    # use if else statement to get where gender is only male else return the user is not male
    # print the first and last name from the json

    if data["gender"] == "male":
        print(data["name"]["first"] + " " + data["name"]["last"])

