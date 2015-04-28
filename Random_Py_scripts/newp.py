def permute(items):
    length = len(items)
    def inner(ix=[]):
        do_yield = len(ix) == length - 1
        for i in range(0, length):
            if i in ix: #avoid duplicates
                continue
            if do_yield:
                yield tuple([items[y] for y in ix + [i]])
            else:
                for p in inner(ix + [i]):
                    yield p
    return inner()
for p in permute([1,2,3,1,2,3,1,2,3]):
    print(p)
