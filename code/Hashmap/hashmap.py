bucket = [
    ["omer", 20],
    ["ali", 30],
    ['talha', 50],
    ['hamza', 60],
]


def searchKey(bucket, key):
    for pair in bucket:
        if pair[0] == key:
            return pair[1]
    return False


print(searchKey(bucket, 'talha'))
