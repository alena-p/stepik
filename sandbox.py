import  requests

data = {
    "title": "Update from charm",
    "gender": "female",
    "link": "https://shop-fe-qa03.befree.ru/zhenskaya",
    "content_block_id": 6,
    "is_active": 1,
    "_method": "PUT",
    "video": None,
    "video_mobile": None
}

# files = {
#     "video": None,
#     "video_mobile": None
# }

headers = {
    "Authorization": "Bearer 169|Og88u0vQKkmmW2ezzlNfnsL6zhohnUDYD0zS8dVEd62ff1b8"
}

response = requests.post(url='https://shop-catalog-qa01.befree.ru/private/v2/content_blocks/6/banner/101', data=data, headers=headers)

print(response.text)
print(response.request.body)