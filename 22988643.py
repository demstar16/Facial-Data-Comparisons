def main(csvfile):
    read_csv(csvfile)
    return

def read_csv(csvfile):
    data = []

    with open(csvfile, 'r') as f:
        for line in f:
            line.strip(',')
            data.append(line)
        

    return

if __name__ == "__main__":
    main("sample_face_data.csv")