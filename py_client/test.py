class Query:
    def __init__(self,time,url,string,userId):
        self.time=time
        self.url=url
        self.string=string
        self.userId=userId
        
def solve(queries):
  dict={}
  for i in queries:
    if((i.url[0:8]=='https://' or i.url[0:7]=='http://') and i.string.isalnum() ):
      usertime=dict.get(i.userId)
      if usertime is None:
        dict[i.userId]=[i.time]
        print("YES")
      elif i.time-usertime<=5:
         print("No")
      else:
        dict[i.userId]=[i.time]
        print("Yes")

query_array= [Query(1, 'https://www.google.com', 'abc', 1), Query(2, 'https://www.google.com', 'abc', 1), Query(3, 'https://www.google.com', 'abc', 1), Query(4, 'https://www.google.com', 'abc', 1), Query(5, 'https://www.google.com', 'abc', 1), Query(6, 'https://www.google.com', 'abc', 1), Query(7, 'https://www.google.com', 'abc', 1), Query(8, 'https://www.google.com', 'abc', 1), Query(9, 'https://www.google.com', 'abc', 1), Query(10, 'https://www.google.com', 'abc', 1), Query(11, 'https://www.google.com', 'abc', 1), Query(12, 'https://www.google.com', 'abc', 1), Query(13, 'https://www.google.com', 'abc', 1), Query(14, 'https://www.google.com', 'abc', 1), Query(15, 'https://www.google.com', 'abc', 1), Query(16, 'https://www.google.com', 'abc', 1), Query(17, 'https://www.google.com', 'abc', 1), Query(18, 'https://www.google.com', 'abc', 1), Query(19, 'https://www.google.com', 'abc', 1), Query(20, 'https://www.google.com', 'abc', 1), Query(21, 'https://www.google.com', 'abc', 1), Query(22, 'https://www.google.com', 'abc', 1), Query(23, 'https://www.google.com', 'abc', 1), Query(24, 'https://www.google.com', 'abc', 1), Query(25, 'https://www.google.com', 'abc', 1), Query(26, 'https://www.google.com', 'abc', 1), Query(27, 'https://www.google.com', 'abc', 1), Query(28, 'https://www.google.com', 'abc', 1), Query(29, 'https://www.google.com', 'abc', 1)]
solve(query_array)