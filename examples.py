"""
GET host.com/users/123  -> 200 {"name": "Krzysztof"... }
DELETE host.com/users/123 -> 200 {"name": "Krzysztof"... } | 204
PUT host.com/users/123 BODY: {"name": "Krzysiu"... } -> 200 {"name": "Krzysiu"... }
PATCH host.com/users/123 BODY: {"name": "Krzysiu"} -> 200 {"name": "Krzysiu"... }

GET host.com/users?offset=0&limit=10 -> 200 [{"name": "Krzysztof", ... }, {"name": "Adrian", ...}, ...]
GET host.com/users?offset=10&limit=10 -> 200 [{"name": "Bonifacy", ... }, {"name": "Anna", ...}, ...]

GET host.com/read_user/123 NOT LIKE THAT!

GET host.com/posts -> 200 [{"author": 123, "text": "lorem ipsum", ... }, {(...)}, {(...)}, ...]
GET host.com/posts/456 -> 200 {"author": 123, "text": "lorem ipsum", ... }
GET host.com/users/123/posts -> 200 [{"author": 123, "text": "lorem ipsum", ... }, {"author": 123, ...}, ...]
GET host.com/users/123/posts/456 -> 200 {"author": 123, "text": "lorem ipsum", ... }
PUT host.com/users/123/posts/456 BODY: {"author": 123, "text": "borem pipsum", ... } -> 200 {"author": 123, "text": "borem pipsum",... }

GET host.com/posts?filter="name:(...)"
POST host.com/posts/filter BODY: {"name": (...)}

"""