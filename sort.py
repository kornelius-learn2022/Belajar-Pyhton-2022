#-----S---Buble sort---------#
real_number_random = [1,5,7,9,10,4,6]

#------Sort From Max---------#
def sort_by_max(data):
    sort_max = data.copy()
    panjang_data = len(sort_max)
    for i in range(len(sort_max)):
        index = panjang_data - i
        for j in range(index-1):
            if sort_max[j] < sort_max[j+1]:
                sort_max[j],sort_max[j+1] = sort_max[j+1],sort_max[j]
    return sort_max

#------Sort From Min---------#
def sort_by_min(data):
    sort_min = data.copy()
    panjang_data = len(sort_min)
    for i in range(len(sort_min)):
        index = panjang_data - i
        for j in range(index-1):
            if sort_min[j] > sort_min[j+1]:
                sort_min[j],sort_min[j+1] = sort_min[j+1],sort_min[j]
    return sort_min

print("Diurutkan dari yang terbesar: ",sort_by_max(real_number_random))
print("Diurutkan dari yang terkecil: ",sort_by_min(real_number_random))

#---- --Merge Sort-------#