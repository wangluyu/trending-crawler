class Message():
    def __init__(self):
        self.img = ""
        self.url = ""
        self.title = ""
        self.ext_img = ""
        self.ext_text = ""
    
    def to_json(self):
        return {
            "img": self.img,
            "url": self.url,
            "title": self.title,
            "ext" : {
                "img": self.ext_img,
                "text": self.ext_text
            }
        }