import settings
import json


class SiteLoader:
    loader = None

    def __init__(self):
        if settings.DATASOURCE == 'json':
            self.loader = JsonLoader()

    def getWebsiteList(self):
        return self.loader.getList()


class JsonLoader:
    def getList(self):
        file = open('website.json')
        content = file.read()
        return json.loads(content)


