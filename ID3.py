import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

data = pd.read_csv('D:\Semester 5_Sally\Pengenalan Pola\Algoritma ID 3\Data Training Kelompok F - Sheet1.csv', on_bad_lines='skip')
#data = pd.read_csv('D:\Semester 5_Sally\Pengenalan Pola\Algoritma ID 3\Data Training Kelompok H - Sheet1.csv', on_bad_lines='skip')
#data = pd.read_csv('D:\Semester 5_Sally\Pengenalan Pola\Algoritma ID 3\Data Training Kelompok J - Sheet1.csv', on_bad_lines='skip')
#data = pd.read_csv('D:\Semester 5_Sally\Pengenalan Pola\Algoritma ID 3\Data Mentah Daun Kelompok D - Sheet1.csv', on_bad_lines='skip')


hasil = [];
status = [];
true = 0;
false = 0;

jumlah_baris = data.shape[0]

for i in range(0, jumlah_baris):
  
  
  data_Id = data['Id']
  test_id = data_Id[i]
  
  
  data_Panjang = data['Panjang']
  test_panjang = data_Panjang[i]
 

  data_Lebar = data['Lebar']
  test_lebar = data_Lebar[i]


  data_Warna = data['Warna']
  test_warna = data_Warna[i]
 

  data_Bentuk = data['Bentuk']
  test_bentuk = data_Bentuk[i]
  

  data_teksturTepi = data['Tekstur Tepi']
  test_teksturTepi = data_teksturTepi[i]
  

  data_Bau = data['Bau']
  test_Bau = data_Bau[i]
  

  data_tulangDaun = data['Tulang Daun']
  test_tulangDaun = data_tulangDaun[i]
  

  data_teksturDaun = data['Tekstur Daun']
  test_teksturDaun = data_teksturDaun[i]
 

  data_motifDaun = data['Motif Daun']
  test_motifDaun = data_motifDaun[i]

  
  if(test_bentuk == 0):
      print("Daun Bunga Kuning Liar")
      hasil.append("Daun Bunga Kuning Liar") 
  elif(test_bentuk == 1):
      print("Daun Sirih Gading")
      hasil.append("Daun Sirih Gading")
  elif(test_bentuk == 4):
      print("Daun Nangka")
      hasil.append("Daun Nangka")
  elif(test_bentuk == 3 and test_teksturTepi == 0):
      print("Daun Ketapang")
      hasil.append("Daun Ketapang")
  elif(test_bentuk == 3 and test_teksturTepi == 1):
      print("Daun Jeruk")
      hasil.append("Daun Jeruk")
  elif(test_bentuk == 3 and test_teksturTepi == 3):
      print("Daun Bayam")
      hasil.append("Daun Bayam")
  elif(test_bentuk == 6 and test_tulangDaun == 1):
      print("Daun Mangga")
      hasil.append("Daun Mangga")
  elif(test_bentuk == 6 and test_tulangDaun == 2):
      print("Daun Glodokan")
      hasil.append("Daun Glodokan")
  elif(test_bentuk == 16 and test_teksturDaun == 0):
      print("Daun Sirsak")
      hasil.append("Daun Sirsak")
  elif(test_bentuk == 16 and test_teksturDaun == 1):
      print("Daun Jambu Biji")
      hasil.append("Daun Jambu Biji")
  else:
      print("Data Daun Tidak Ditemukan")   
      hasil.append("Data Daun Tidak Ditemukan")
      
      
  if(data_Id[i] == hasil[i]):
      print("True")
      true += 1;
      status.append("True")
  else:
      print("False")
      false +=1;
      status.append("False")
        
data["akhir"] = hasil

data["status"] = status

print(data);

print("jumlah data training yang kami ambil : ",data['Id'].count());

print("jumlah True : ",true);
akurasiTrue = ((true/data['Id'].count())*(100/100*100));
coba1 = np.ceil(akurasiTrue);
print("Akurasi True = ",coba1,"%");
    
print("jumlah False : ",false);
akurasiFalse = ((false/data['Id'].count())*(100/100*100));
coba2 = np.ceil(akurasiFalse);
print("Akurasi False = ",coba2,"%");


