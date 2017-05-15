from nose.tools import *
from pyquiz.quiz5 import *

EMPTY = ((), {})

class TestQuiz5(object):
    def setUp(self):
        self.inst = Cow()

    def test_should_record_past_function_calls(self):
        for _ in range(4):
            self.inst.moo()

        assert_equal(len(self.inst.moo_history), 4)

    def test_should_record_past_arguments_passed_to_function(self):
        expected_history = [EMPTY, (('corn',), {}), (('nachos',), {})]
        self.inst.chew()
        self.inst.chew('corn')
        self.inst.chew('nachos')

        assert_equal(self.inst.chew_history, expected_history)

    def test_should_record_past_keyword_arguments(self):
        expected_history = [EMPTY, ((), {'food': 'corn'}), ((), {'food': 'nachos'})]
        self.inst.chew()
        self.inst.chew(food='corn')
        self.inst.chew(food='nachos')

        assert_equal(self.inst.chew_history, expected_history)

    def test_should_record_past_args_and_kwargs_passed_to_function(self):
        expected_history = [EMPTY, (('corn',), {}), (('nachos',), {}), ((), {'food': 'corn'}), ((), {'food': 'nachos'})]
        self.inst.chew()
        self.inst.chew('corn')
        self.inst.chew('nachos')
        self.inst.chew(food='corn')
        self.inst.chew(food='nachos')

        assert_equal(self.inst.chew_history, expected_history)

    def test_should_record_history_of_different_functions(self):
        expected_history = [EMPTY, (('corn',),{}), ((), {'food': 'nachos'})]
        self.inst.chew()
        self.inst.chew('corn')
        self.inst.chew(food='nachos')
        self.inst.moo()
        self.inst.moo()

        assert_equal(self.inst.chew_history, expected_history)
        assert_equal(self.inst.moo_history, [EMPTY, EMPTY])

    def test_should_record_history_of_different_instances(self):
        expected_history = [(('nachos',), {})]
        jessie_expected_history = [(('grass',), {})]
        self.inst.chew('nachos')

        jessie = Cow()
        jessie.chew('grass')

        assert_equal(self.inst.chew_history, expected_history)
        assert_equal(jessie.chew_history, jessie_expected_history)


class Cow(object):
    name = 'Dan'
    @historian
    def moo(self):
        return self.name

    @historian
    def chew(self, food='hay'):
        return self.name
