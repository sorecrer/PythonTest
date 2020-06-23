import pandas as pd


def main():
    csv_data = pd.read_csv('Q8.csv', encoding='gbk')
    csv_data = csv_data.to_dict(orient='records')
    for data in csv_data:
        print(data)


if __name__ == '__main__':
    main()
