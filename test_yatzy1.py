from yatzy1 import Yatzy


# These unit tests can be run using the py.test framework
# available from http://pytest.org/

def test_chance_scores_sum_of_all_dice():
    expected = 15
    actual = Yatzy([2, 3, 4, 5, 1]).chance()
    assert expected == actual
    assert 16 == Yatzy([3, 3, 4, 5, 1]).chance()


def test_yatzy_scores_50():
    expected = 50
    actual = Yatzy([4, 4, 4, 4, 4]).yatzy()
    assert expected == actual
    assert 50 == Yatzy([6, 6, 6, 6, 6]).yatzy()
    assert 0 == Yatzy([6, 6, 6, 6, 3]).yatzy()


def test_sum_by_number():
    assert 1 == Yatzy([1, 2, 3, 4, 5]).sum_by_number(1)
    assert 2 == Yatzy([1, 2, 1, 4, 5]).sum_by_number(1)

    assert 4 == Yatzy([1, 2, 3, 2, 6]).sum_by_number(2)
    assert 10 == Yatzy([2, 2, 2, 2, 2]).sum_by_number(2)

    assert 6 == Yatzy([1, 2, 3, 2, 3]).sum_by_number(3)
    assert 12 == Yatzy([2, 3, 3, 3, 3]).sum_by_number(3)

    assert 12 == Yatzy([4, 4, 4, 5, 5]).sum_by_number(4)
    assert 4 == Yatzy([4, 5, 5, 5, 5]).sum_by_number(4)

    assert 15 == Yatzy([4, 4, 5, 5, 5]).sum_by_number(5)
    assert 20 == Yatzy([4, 5, 5, 5, 5]).sum_by_number(5)

    assert 0 == Yatzy([4, 4, 4, 5, 5]).sum_by_number(6)
    assert 6 == Yatzy([4, 4, 6, 5, 5]).sum_by_number(6)


def test_one_pair():
    assert 6 == Yatzy([3, 4, 3, 5, 6]).one_pair()
    assert 10 == Yatzy([5, 3, 3, 3, 5]).one_pair()
    assert 12 == Yatzy([5, 3, 6, 6, 5]).one_pair()


def test_two_pair():
    assert 16 == Yatzy([3, 3, 5, 4, 5]).two_pair()
    assert 18 == Yatzy([3, 3, 6, 6, 6]).two_pair()
    assert 0 == Yatzy([3, 3, 6, 5, 4]).two_pair()


def test_three_of_a_kind():
    assert 9 == Yatzy([3, 3, 3, 4, 5]).three_of_a_kind()
    assert 15 == Yatzy([5, 3, 5, 4, 5]).three_of_a_kind()
    assert 9 == Yatzy([3, 3, 3, 3, 5]).three_of_a_kind()


def test_four_of_a_kind():
    assert 12 == Yatzy([3, 3, 3, 3, 5]).four_of_a_kind()
    assert 20 == Yatzy([5, 5, 5, 4, 5]).four_of_a_kind()
    assert 12 == Yatzy([3, 3, 3, 3, 3]).four_of_a_kind()
    assert 0 == Yatzy([3, 3, 3, 2, 1]).four_of_a_kind()


def test_small_straight():
    assert 15 == Yatzy([1, 2, 3, 4, 5]).small_straight()
    assert 15 == Yatzy([2, 3, 4, 5, 1]).small_straight()
    assert 0 == Yatzy([1, 2, 2, 4, 5]).small_straight()


def test_large_straight():
    assert 20 == Yatzy([6, 2, 3, 4, 5]).large_straight()
    assert 20 == Yatzy([2, 3, 4, 5, 6]).large_straight()
    assert 0 == Yatzy([1, 2, 2, 4, 5]).large_straight()


def test_full_house():
    assert 18 == Yatzy([6, 2, 2, 2, 6]).full_house()
    assert 0 == Yatzy([2, 3, 4, 5, 6]).full_house()
