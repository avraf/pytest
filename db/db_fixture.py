students = (('Jon Sanders', 24, 'A14', 88),
            ('Don Simmons', 24, 'B52', 78),
            ('Bobby Jones', 22, 'A14', 91),
            ('Eric Snowden', 19, 'E11', 82))

faculty = (('Mr. Stein', 'principal', 'B00'),
            ('Mrs. Davids', 'teacher', 'A14'))

rooms = (('B00', "principal's office"),
            ('A00', 'gym'))

class Row(object):
    def __init__(self, columns=None, values=None, key_val_pairs=None):
        for column, value in zip(columns, values):
            self.__dict__[column] = value

    def __getitem__(self, column):
        return self.__dict__[column]

    # For debugging purposes
    def __repr__(self):
        return ' | '.join("{}: {}".format(*col) for col in self.__dict__.iteritems())

student_columns = ('name', 'age', 'room_number', 'average')
faculty_columns = ('name', 'job', 'room_number')
room_columns    = ('number', 'room_type')

a_db = {'students': [Row(student_columns, s) for s in students],
        'faculty': [Row(faculty_columns, f) for f in faculty],
        'rooms': [Row(room_columns, r) for r in rooms]}
