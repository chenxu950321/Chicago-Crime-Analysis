import input as input

def main(): 
    '''
    shape
    (2, 6)
    statistics
            District  Latitude  Longitude
    count   2.000000       2.0        2.0
    mean   11.500000       0.0        0.0
    std     9.192388       0.0        0.0
    min     5.000000       0.0        0.0
    25%     8.250000       0.0        0.0
    50%    11.500000       0.0        0.0
    75%    14.750000       0.0        0.0
    max    18.000000       0.0        0.0
    data samples 10 rows
                                        Date     Description  District Primary Type  Latitude  Longitude
    idx
    2017-04-01 11:05:00  04/01/2017 11:05:00 AM   FROM BUILDING        18        THEFT       0.0        0.0
    2017-03-20 21:05:00  03/20/2017 09:05:00 PM  $500 AND UNDER         5        THEFT       0.0        0.0
                                        Date     Description  District Primary Type  Latitude  Longitude
    idx
    2017-04-01 11:05:00  04/01/2017 11:05:00 AM   FROM BUILDING        18        THEFT       0.0        0.0
    2017-03-20 21:05:00  03/20/2017 09:05:00 PM  $500 AND UNDER         5        THEFT       0.0        0.0
    '''
    path = r"src\crime.csv"
    iii = input.Input(path)

    row_num = 10000
    col_name = ['Date', 'Description', 'District', 'Primary Type', 'Latitude', 'Longitude']
    year = 2017
    nan_not_allowed = 1
    primary_type = 'THEFT'
    time_range = ['2017-03-20', '2017-4-01'] 
    arrest = 2
    s = iii.data_extract(row_num, col_name, year, nan_not_allowed, primary_type, time_range, arrest)
    print(s)
if __name__ == "__main__":
    main()