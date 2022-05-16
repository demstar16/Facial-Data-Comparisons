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
    return 

#function to read all of the csvfile
def read_csv(csvfile):
    data = []
    try:
        with open(csvfile, 'r') as f:
            #stores the order of the data given
            for line in f:
                header = line
                break
            next(f) #skips the header when gathering data
            #obtain all the data
            for line in f:
                currentline = line.split(",")
                data.append((str(currentline[0]), str(currentline[1]), float(currentline[2]), 
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

'''
data = read_csv("sample_face_data.csv")
wanted_data = data_sort(data, ['A4722', 'B1080'])
for i in wanted_data:
    print(i)
'''
print(main("sample_face_ata.csv", ['a4722', 'b1080']))

