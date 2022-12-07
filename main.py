import requests
import json

def main():
    token = input("Enter your token: ")
    channel = input("Enter channel id: ")
    savepins(token, channel)

def savepins(token, channel):
    headers = {"Authorization": token}
    r = requests.get(f"https://discord.com/api/v8/channels/{channel}/pins", headers=headers).json()
    f = open("pins.json", "w")
    final = []
    for i in r:
        final.append({"content": i["content"], "attachments": i["attachments"], "author": i["author"]["username"], "author_id": i["author"]["id"]})
    f.write(json.dumps(final, indent=4))
    # final = {}
    # for i in r:
    #     final[i["id"]] = i["content"]
    #     if i["attachments"]:
    #         final[i["id"]] += f" {i['attachments'][0]['url']}"
    #         final += "\n"
    #f.write(str(final))

if __name__ == "__main__":
    main()        