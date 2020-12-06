def data_Stat(x):
    hasil = []
    for i in x :
        list_bil = list(x)
        a = sum(list_bil)/len(list_bil)
        b = max(list_bil)
        c = min(list_bil)
        hasil = [a, b, c]
    return hasil

x = [7, 6, 5, 4]
print(data_Stat(x))
