# 阿拉伯數字轉為中文
def int_to_chine(trans_num):
    
    num = {0:"零", 1:"一",2:"二",3:"三",4:"四",5:"五",6:"六", 7:"七",8:"八",9:"九",}
    tmp = []
    floor=''
    #每個數字存入陣列中，最後再從後面一個一個取出
    while trans_num !=0:
        get_number = trans_num %10
        if get_number in num:
            tmp.append(num[get_number])
        trans_num = trans_num//10
    floor+=''.join( tmp[::-1])

    return floor