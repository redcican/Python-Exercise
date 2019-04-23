# dynamic filter the unique value of a list

products = [
    {
        "title": "Iphone 8",
        "company": "apple"
    },
    {
        "title": "Galaxy",
        "company": "samsung"
    },
    {
        "title": "Iphone 7",
        "company": "apple"
    },
    {
        "title": "Iphone Xs",
        "company": "apple"
    },
    {
        "title": "HTC Phone",
        "company": "htc"
    },
]

unique_company = []

def getUnique(arr):
    for company in arr:
        s = company["company"]
        unique_company.append(s)
    return set(unique_company)


print(getUnique(products))