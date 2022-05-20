__author__ = "Dempsey Thompson - 22988643"
__version__ = "1.0"

def main(csvfile, adultIDs):
    #read the csvfile
    data = read_csv(csvfile)

    #make the adultIDs case insensitive
    for i in range(len(adultIDs)):
        adultIDs[i] = adultIDs[i].upper()

    #trim the data, so we just have what we want
    wanted_data = data_sort(data, adultIDs)

    #splits the adults up
    adult1 = wanted_data[:15]
    adult2 = wanted_data[15:]

    #gain euclidean distances for each adult
    euclidean_dict1 = euclidean_dist_dict(adult1)
    euclidean_dict2 = euclidean_dist_dict(adult2)

    #create our OP1 return variable
    OP1 = [euclidean_dict1, euclidean_dict2]

    #create our OP2 return variable
    OP2 = cosine_sim(euclidean_dict1, euclidean_dict2)

    return OP1, OP2

#function to read all of the csvfile
def read_csv(csvfile):
    data = []
    try:
        with open(csvfile, 'r') as f:
            #stores the order of the data given
            header = f.readline()
            
            #obtain all the data
            for line in f:
                currentline = line.split(",")
                data.append((str(currentline[0]).upper(), str(currentline[1]).upper(), float(currentline[2]), 
                float(currentline[3]), float(currentline[4])))
    except FileNotFoundError:
        print("Error finding or opening the file.")
  
    return data

#function to sort the data from the csvfile
def data_sort(data, adultIDs):
    wanted_data = []
    for i in range(len(data)):
        if data[i][0] == adultIDs[0] or data[i][0] == adultIDs[1]:
            wanted_data.append(data[i])
    return wanted_data

#function to help sort the data into what facial area they are for
def euclidean_sort(data):
    face_dist_names = ['FW', 'OCW', 'LEFL', 'REFL', 'ICW', 'NW', 'ABW', 'MW', 'NBL', 'NH']
    euclidean_dist = {i: [] for i in face_dist_names}   
    for i in range(len(data)):
        if data[i][1] == 'EX_L':
            euclidean_dist['OCW'].insert(1, data[i])
            euclidean_dist['LEFL'].insert(1, data[i])

        elif data[i][1] == 'EN_L':
            euclidean_dist['LEFL'].insert(0, data[i])
            euclidean_dist['ICW'].insert(1, data[i])

        elif data[i][1] == 'N':
            euclidean_dist['NBL'].insert(1, data[i])
            euclidean_dist['NH'].insert(1, data[i])

        elif data[i][1] == 'EN_R':
            euclidean_dist['REFL'].insert(1, data[i])
            euclidean_dist['ICW'].insert(0, data[i])

        elif data[i][1] == 'EX_R':
            euclidean_dist['OCW'].insert(0, data[i])
            euclidean_dist['REFL'].insert(0, data[i])

        elif data[i][1] == 'PRN':
            euclidean_dist['NBL'].insert(0, data[i])

        elif data[i][1] == 'AL_L':
            euclidean_dist['NW'].insert(1, data[i])
            
        elif data[i][1] == 'AL_R':
            euclidean_dist['NW'].insert(0, data[i])
            
        elif data[i][1] == 'SBAL_L':
            euclidean_dist['ABW'].insert(1, data[i])

        elif data[i][1] == 'SBAL_R':
            euclidean_dist['ABW'].insert(0, data[i])

        elif data[i][1] == 'CH_L':
            euclidean_dist['MW'].insert(1, data[i])

        elif data[i][1] == 'CH_R':
            euclidean_dist['MW'].insert(0, data[i])

        elif data[i][1] == 'SN':
            euclidean_dist['NH'].insert(0, data[i])

        elif data[i][1] == 'FT_L':
            euclidean_dist['FW'].insert(1, data[i])

        elif data[i][1] == 'FT_R':
            euclidean_dist['FW'].insert(0, data[i])

    return euclidean_dist


#takes a dictionary
#The 3D distance between two points A = (x1, y1, z1) and B = (x2, y2, z2) in cartesian plain
def euclidean_dist_dict(adultID_data):
    face_dist_names = ['FW', 'OCW', 'LEFL', 'REFL', 'ICW', 'NW', 'ABW', 'MW', 'NBL', 'NH']
    euclidean_distances = {i:None for i in face_dist_names}
    sorted_dict = euclidean_sort(adultID_data)

    for abvn in sorted_dict.keys():
        val1 = 0
        val2 = 0
        val3 = 0
       
        for face_feat in sorted_dict[abvn]:
            if val1 == 0 and val2 == 0 and val3 == 0:
                val1 += face_feat[2]
                val2 += face_feat[3]
                val3 += face_feat[4]
                
            else:
                val1 -= face_feat[2]
                val2 -= face_feat[3]
                val3 -= face_feat[4]
        
        euc_formula = ((val1**2) + (val2**2) + (val3**2))**0.5
        euclidean_distances[abvn] = round(euc_formula,4)
 
    return euclidean_distances

def cosine_sim(dict1, dict2):
    cosine_similarity = 0
    sum_of_multiples = 0
    if len(dict1) == len(dict2):
        for key1, key2 in zip(dict1, dict2):
            sum_of_multiples += (dict1[key1] * dict2[key2])

    dict1_sqr_rt_vals = sum_under_sqr_rt(dict1)
    dict2_sqr_rt_vals = sum_under_sqr_rt(dict2)

    cosine_similarity = (sum_of_multiples) / (dict1_sqr_rt_vals * dict2_sqr_rt_vals)
    return round(cosine_similarity,4)

def sum_under_sqr_rt(dict):
    sum = 0
    for i in dict.values():
        sum += i**2
    return sum**0.5    

'''
data = read_csv("sample_face_data.csv")
wanted_data = data_sort(data, ['R7033', 'P1283'])

adult1 = wanted_data[:15]
euclidean_vals1 = euclidean_dist_dict(adult1)

sum_under_sqr_rt(euclidean_vals1)

adult2 = wanted_data[15:]
euclidean_vals2 = euclidean_dist_dict(adult2)

OP1 = []
OP1.append(euclidean_vals1)
OP1.append(euclidean_vals2)


cosine_sim(OP1[0], OP1[1])

print(OP1)
'''

OP1, OP2 = main("sample_face_data.csv", ['r7033', 'P1283'])
print(OP1)
print(OP2)
