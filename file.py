#读文件，将每一行的和写入文件
def readfile(filename):
    f1 = open("sum.txt","w")
    list2 = []
    with open(filename,"r") as f:
        list1 = f.readlines()
    for i in range(len(list1)):
        list1[i] = list1[i].strip()
        list2=list1[i].split(",")
        sum=int(list2[0])+int(list2[1])
        f1.write(str(sum)+"\n")
    f1.close()
if __name__ == "__main__":
    readfile("data.dat")
    