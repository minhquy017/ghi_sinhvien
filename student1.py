class SinhVien:
    def __init__(self,name,age,score):
        self.hoten=name
        self.tuoi=age
        self.dtb=score

    def __str__(self):
        message = "[hoten: " + self.hoten + "; tuoi:" + str(self.tuoi) + "; dtb: " + str(self.dtb) + "]"
        return message
    def __gt__(self, obj):
        return (self.dtb>obj.dtb)
    def __ge__(self,obj):
        return (self.dtb >= obj.dtb)
    def __lt__(self,obj):
        return (self.dtb < obj.dtb)
    def __le__(self,obj):
        return (self.dtb <= obj.dtb)
    def __eq__(self,obj):
        return (self.dtb==obj.dtb)

