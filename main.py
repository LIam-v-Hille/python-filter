from filter import Filter

test = Filter()
test.add_filter_phrase("flight","baseball","dad","lady","plane")
test.filter_file('test.txt',False,True,'log.txt')
print(test.get_inf())
