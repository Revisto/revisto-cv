import json


class Files:
    def get_social_urls(self):
        file = open("social_urls.json")
        data = json.load(file)
        file.close()
        return data["socials"]
