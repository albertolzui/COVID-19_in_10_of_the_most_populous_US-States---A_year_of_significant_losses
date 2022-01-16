def get_month(month):
    switcher={
'01':'January',
'02':'February',
'03':'March',
'04':'April',
'05':'May',
'06':'June',
'07':'July',
'08':'August',
'09':'September',
'10':'October',
'11':'November',
'12':'December'
}

    return switcher.get(month)




def get_date(data):
    date_fetcher = data.iloc[[0], [0]]
    date_refiner = date_fetcher.iloc[0]
    date_format = date_refiner.submission_date
    actual_date = date_format.replace("T00:00:00.000", "")

    return actual_date



