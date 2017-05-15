from nose.tools import *
from pyquiz.quiz6 import select
from pyquiz.db.db_fixture import a_db

select.db = a_db

students = 'students'
ERIC = 'Eric Snowden'

class TestQuiz6(object):
    def test_should_query_a_whole_table(self):
        rooms = 'rooms'
        actual_query = select('*').from_table(rooms)()
        expected_query = a_db[rooms]

        assert_equal(actual_query, expected_query)

    def test_should_query_only_specified_columns(self):
        wanted_columns = 'name', 'average'

        queried_row = select(*wanted_columns).from_table(students)()[0]

        assert all(result_column in wanted_columns
                    for result_column in queried_row.keys())

    def test_should_filter_query(self):
        expected_student = ERIC
        actual_query = select('*') \
                        .from_table(students)(
                        where=lambda r: r.age < 20)

        assert_equal(actual_query[0]['name'], expected_student)

    def test_should_filter_query_by_unwanted_column(self):
        expected_student = ERIC
        actual_query = select('name') \
                        .from_table(students)(
                        where=lambda r: r.age < 20)

        assert_equal(actual_query[0]['name'], expected_student)

    def test_should_order_query_by_a_column(self):
        col_to_order_by = 'average'
        actual_query = select('*') \
                        .from_table(students)(
                            order_by=col_to_order_by)

        expected_query = sorted(a_db[students], key=lambda s: s[col_to_order_by])

        assert_equal(actual_query, expected_query)

    def test_should_order_query_by_a_column_descending(self):
        order_by_request = 'average desc'
        actual_query = select('*') \
                        .from_table(students)(
                            order_by=order_by_request)

        expected_query = sorted(a_db[students], key=lambda s: s['average'], reverse=True)

        assert_equal(actual_query, expected_query)

    def test_should_filter_and_order_by_specific_columns(self):
        wanted_columns = 'name', 'average'
        col_to_order_by = 'average asc'
        actual_query = select(*wanted_columns) \
                        .from_table(students)(
                        where=lambda r: r.average > 80 and \
                                        r.room_number == 'A14',
                        order_by=col_to_order_by)

        expected_query = [{'name': 'Jon Sanders', 'average': 88},
                            {'name': 'Bobby Jones', 'average': 91}]

        assert_equal(actual_query, expected_query)
