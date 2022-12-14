from student1 import SinhVien
import os
import pickle
def ghi_sinh_vien(thumuc : str , tap_tin:str , obj :SinhVien):
    try:
        with open(os.path.join(thumuc,tap_tin),"wb") as f:
            pickle.dump(obj,f)
        print("hoàn thành")
    except Exception as e:
        print("xảy ra lỗi")
def doc_sinhvien(thumuc:str,tap_tin:str)->SinhVien:
    try:
        with open(os.path.join(thumuc,tap_tin),"rb")as f:
            sv=pickle.load(f)
        return sv
    except Exception as e:
        return None
def main():
    path= "C:/Users/MINH QUY"
    filename = "doc.dat"
    sv1 = SinhVien("minh quý",18,10.0)
    x = ghi_sinh_vien(path,filename,sv1)
    noidung = doc_sinhvien(path,filename)
    print(noidung)
    print("kết thúc chương trình")

if __name__=="__main__":
    main()