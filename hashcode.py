books_count, libs_count, deadline =  [int(x) for x in input().split(" ")]
book_scores = [int(x) for x in input().split(" ")]
b_count_lib = []; su_time = []; scan_lim = []; book_ids = []
for _ in range(libs_count):
    n_,t_,m_ = [int(x) for x in input().split(" ")]
    b_count_lib.append(n_); su_time.append(t_); scan_lim.append(m_)
    book_ids.append(input().split(" "))
#print(books_count,libs_count ,deadline)
#print(book_scores)
#print(b_count_lib, su_time, scan_lim, book_ids)

score = []
for i in range(libs_count):
    sum = 0
    for j in book_ids[i]:
        sum += book_scores[int(j)]
    score.append(sum)

lib_rating = []
for i in range(libs_count):
    # r = #calculate rating for each library
    if su_time[i] >= deadline:
        continue
    r = (score[i]*scan_lim[i])/su_time[i]
    #print(r)
    lib_rating.append(tuple([i, r, su_time[i]]))
lib_rating = sorted(lib_rating, key = lambda x:x[1], reverse=True)

rate = []
for i in range(len(lib_rating)):
    rate.append(lib_rating[i][1])
#print(rate)

rvalue, i, c = 0, 0, 0
while i < len(lib_rating):
    rvalue = lib_rating[i][1]
    c = rate.count(rvalue)
    if c > 1:
        lib_rating[i:i+c] = sorted(lib_rating[i:i+c], key = lambda x:x[2], reverse=True)
    i = i+c

count = 0
books = []
libs = []
b_set = set()

for i in range(len(lib_rating)):
    lib_num  = lib_rating[i][0]
    if su_time[lib_num] >= (deadline - count):
        continue
    z = []
    for _ in book_ids[lib_num]:
        if _ not in b_set:
            z.append(_)
    if len(z) == 0:
        continue
    books.append(tuple([z, scan_lim[i]*(deadline-count)]))
    libs.append(lib_num)
    b_set.update(z)

print(len(libs))
for i in range(len(libs)):
    #if(books[i][0].__len__ <books[i][1]):
    #    print(books[i][0])
    #   print(books[i][0][0:books[i][1]])
    num = min(len(books[i][0]), books[i][1])
    print(libs[i], num)
    print(*books[i][0][0:num])