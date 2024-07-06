class Result():

    def __init__(self):
        self.code = 100
        self.msg = ""
        self.data = ""

    def success(self, url, data):
        self.code = 200
        self.msg = "🎉 Congardulations, handling {} successfully.".format(url)
        self.data = data
        return self

    def failed(self, url, data):
        self.code = 500
        self.msg = " ⚠️ Error! Handle {} failed!".format(url)
        self.data = data
        return self
