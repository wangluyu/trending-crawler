class Message():
    def __init__(self):
        self.img = ""
        self.url = ""
        self.title = ""
        self.ext_img = ""
        self.ext_text = ""
        self.ext = None
    
    def to_json(self):
        if self.ext is not None:
            ext = self.ext
        else:
            ext = {
                "img": self.ext_img,
                "text": self.ext_text
            }
        return {
            "img": self.img,
            "url": self.url,
            "title": self.title,
            "ext" : ext
        }