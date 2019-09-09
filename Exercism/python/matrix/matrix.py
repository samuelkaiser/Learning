the_matrix = "9 8 7\n5 3 2\n6 6 7"
# print(the_matrix)

class Matrix(object):
    def __init__(self, matrix_string):
        pass

    def row(self, index):
        rows = list()
        for line in the_matrix.splitlines():
            rows.append(list(line.split()))

        for row in rows:
            print(rows)

        #print(rows)
        #pass

    def column(self, index):
        pass

x = Matrix(the_matrix)

x.row(the_matrix);
