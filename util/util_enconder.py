from json import JSONEncoder

class Util_encoder(JSONEncoder):
    def default(self, obj):
        return obj.__dict__