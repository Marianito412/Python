class StringHandler:
    no_tag_found = False 
    def extention(self):
        C = str(self)
        return "."+C.split(".")[-1]

    def tag(self):
        A = str(self)
        tag = A.split("'")[0]
        if A == tag:
            return "No Tag Found"
        else:
            return tag

    def name(self):
        try:
            B = str(self)
            return B.split(".")[0].split("'")[1]
        except:
            B = str(self)
            return B.split(".")[0]

