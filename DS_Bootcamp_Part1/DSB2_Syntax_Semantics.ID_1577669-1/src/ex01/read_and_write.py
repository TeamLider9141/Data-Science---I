def read_and_write():
    with open('ds.csv', 'r') as infile, open('ds.tsv', 'w') as outfile:
        for line in infile:
            columns = line.rstrip('\n').split(',')
            outfile.write('\t'.join(columns) + '\n')


if __name__ == '__main__':
    read_and_write()
    #to run it => python3 read_and_write.py
