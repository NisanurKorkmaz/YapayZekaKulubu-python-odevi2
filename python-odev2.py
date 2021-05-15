#txt'den ozel karakterleri ve sayilari sildirip temizleme

file=open("odev.txt","r")
newfile=open("temiz.txt","w")

line=file.readline()
newline=""

while line :
    
    for i in range(len(line)): #satir icinde dolasim
        if line[i].isalpha():
            newline+=line[i]
            
    print(newline)
    newfile.write(newline) #temiz txt'ye veri aktarimi
    newfile.write("\n")
    newline="" #degsiken temizleme
    
    line=file.readline() #bir sonraki satira gecis

file.close()
newfile.close()
