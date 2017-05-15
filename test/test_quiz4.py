from nose.tools import *
from pyquiz.quiz4 import *

class TestQuiz4(object):
    def test_should_be_healthy_when_initialized_with_calories_less_than_200(self):
        apple = Dessert('apple', 199)
        assert_true(apple.is_healthy)

    def test_should_be_unhealthy_when_initialized_with_calories_not_less_than_200(self):
        apple = Dessert('candied apple', 200)
        assert_false(apple.is_healthy)
        
    def test_should_be_delicious(self):
        apple = Dessert('candied apple', 200)
        assert_true(apple.is_delicious)

    def test_should_be_unhealthy_when_was_healthy_but_now_unhealthy(self):
        apple = Dessert('apple', 5)
        assert_true(apple.is_healthy)

        apple.calories = 201
        assert_false(apple.is_healthy)

    def test_should_be_healthy_when_was_unhealthy_but_now_healthy(self):
        apple = Dessert('candied apple', 222)
        assert_false(apple.is_healthy)

        apple.calories = 7
        assert_true(apple.is_healthy)

    def test_should_be_not_delicious_when_flavor_was_not_licorice_but_now_is(self):
        apple_jelly_bean = JellyBean('apple jelly bean', 209, 'sour apple')
        assert_true(apple_jelly_bean.is_delicious)

        apple_jelly_bean.flavor = "black licorice"
        assert_false(apple_jelly_bean.is_delicious)

    def test_should_be_delicious_when_flavor_was_licorice_but_now_is_not(self):
        apple_jelly_bean = JellyBean('jelly bean', 209, 'black licorice')
        assert_false(apple_jelly_bean.is_delicious)

        apple_jelly_bean.flavor = 'sour apple'
        assert_true(apple_jelly_bean.is_delicious)
