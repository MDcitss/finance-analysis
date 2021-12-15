import csv
import pandas as pd

def extract_csv(file_open):
    file = open(file_open)
    file_csv = csv.reader(file)
    return file_csv

def common_member(a, b):
    a_set = set(a)
    b_set = set(b)
    if len(a_set.intersection(b_set)) > 0:
        return(True) 
    return(False)  

def main():
    bank_statement = pd.read_excel("bank.xlsx")
    # print(bank_statement.columns[1])
    total_spending = 0
    for i in bank_statement['Unnamed: 1']:
        total_spending += i
        # print(i)
        # print(bank_statement[str(i)])
    print(total_spending)

    for i in bank_statement['Unnamed: 2']:
        category_str = i.split()
        print(category_str)
    # bank_statement.
    # print(bank_statement)
    # for i in bank_statement:
    #     print(i)

# Gets .csv bank statement

if __name__ == '__main__':
    main()
