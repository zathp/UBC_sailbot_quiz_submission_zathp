from standard_calc import bound_to_180, is_angle_between


""" Tests for bound_to_180() """


def test_bound_basic1():
    assert bound_to_180(0) == 0
    assert bound_to_180(180) == -180
    assert bound_to_180(210) == -150
    assert bound_to_180(-180) == -180
    assert bound_to_180(-210) == 150
    assert bound_to_180(750) == 30
    assert bound_to_180(-750) == -30
    print("bound basic 1 Passed")


""" Tests for is_angle_between() """


def test_between_basic1():
    assert is_angle_between(0, 1, 2)
    assert is_angle_between(120, 180, 330) == False
    assert is_angle_between(330, 180, 120) == False
    assert is_angle_between(120, 90, 330)
    assert is_angle_between(330, 90, 120)
    assert is_angle_between(90, 120, 180)
    assert is_angle_between(180, 120, 90)
    assert is_angle_between(90, 210, 180) == False
    assert is_angle_between(180, 210, 90) == False
    assert is_angle_between(270, 30, 330) == False
    assert is_angle_between(30, 30, 30)
    assert is_angle_between(-30, 0, 30)
    assert is_angle_between(30, 30, 90)
    assert is_angle_between(30, 90, 90)


test_bound_basic1()
test_between_basic1()