url_search = "<https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>"
_, query = url_search.split('?')
print(query)

params = query.split('&')
print(params)

obj_query = {}
for el in params:
    key, value = el.split('=')
    obj_query.update({key: value.replace('+', ' ').replace('>', '')})
print(obj_query)