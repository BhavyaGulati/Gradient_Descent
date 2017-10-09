import pandas as pd #To load in the data

def get_data(path='tryData.csv', cols = ['TV_comm','Sales'], n_rows = 1000):
    df = pd.read_csv(path) #Reads in the CSV file specified
    df = df[cols] #Gets only the specified columns
    df.fillna(0, inplace = True) #Replaces missing values with 0.
    arr = df.iloc[:n_rows].as_matrix() #returns the dataframe as a python array.
    print(arr[:2,:])

    return arr

if __name__=='__main__':
    get_data('tryData.csv') #Driver to test the function.