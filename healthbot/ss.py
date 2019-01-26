import requests

def sg(a):
    data = requests.get("https://ghibliapi.herokuapp.com/films").json()
    for mydict in data:
        if a.lower() == mydict.get("title").lower():
            return "**Synopsis :** " + mydict.get("description") + "\n"+"**Director : **" + mydict.get("director") + "\n"+"**Producer : **" +mydict.get("producer") + "\n"+ "**Release Date : **" + mydict.get("release_date")+ "\n"+"**RT Score : **" + mydict.get("rt_score")
    
    return "Not Found"

# def main():
#     a = input("Enter"
# )
#     p = sg(a)
#     print(p)

# main()
# print(data)
