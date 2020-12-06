def sortStringByChair(my_Data):
    my_Data.sort(reverse = True)
    return my_Data

my_Data = ['apel','rambutan','jeruk']
print("sebagai contoh: \n diberikan sebuah list myData =" + str(my_Data))
datasorted = sortStringByChair(my_Data)
print("jika dipanggil function tersebut,maka akan dihasilkan data list yang baru dengan susunan :" +"\n" + str(datasorted))
