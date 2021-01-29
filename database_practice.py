
def put_in_db(line_items):
    

def read_all_that_data():

    f = open("./interview_test_data_small.csv", "r")

    for line in f:

        line_items = line.split(sep=',')
        put_in_db(line_items)
    
    f.close

if __name__ == "__main__":
    read_all_that_data()
