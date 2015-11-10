"""
Test that pickle and dill output the same bytes
"""

import nose


def global_func():
    pass


# def test_dumps_eq():
#     # Test that dill and pickle produce the same results
#     nose.tools.assert_equal(dill.dumps(1), pickle.dumps(1))
#     nose.tools.assert_equal(dill.dumps({'a': 0, 'b': 1}), pickle.dumps({'a': 0, 'b': 1}))
#     nose.tools.assert_equal(dill.dumps(global_func), pickle.dumps(global_func))
