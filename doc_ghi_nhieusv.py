from student1 import SinhVien
import os
import pickle
def ghi_sinh_vien(thumuc : str , tap_tin:str , objs :SinhVien):
    try:
        with open(os.path.join(thumuc,tap_tin),"wb") as f:
            pickle.dump(objs,f)
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
def in_list_sinhvien(content: list[SinhVien]):
    for item in content :
        print(item)
def main():
    path= "C:/Users/MINH QUY"
    filename = "doc1.dat"
    sv1 = [SinhVien("minh quý",18,10.0),
           SinhVien("quang quý",18,9.0),
           SinhVien("lê  quý",18,8.0),
           SinhVien("hoàng  quý",18,7.0)]
    x = ghi_sinh_vien(path,filename,sv1)
    noidung = doc_sinhvien(path,filename)
    in_list_sinhvien(noidung)
    print("kết thúc chương trình")

if __name__=="__main__":
    main()
