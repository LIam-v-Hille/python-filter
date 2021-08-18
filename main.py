from filter import Filter

test = Filter()
test.add_filter_phrase("rob van hille","nIcky van hille","dad cEll")
test.filter_file('_chat.txt',False,True,'log.txt',multiword=True)
print(test.get_inf())
