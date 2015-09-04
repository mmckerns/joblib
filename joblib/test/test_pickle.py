"""
Test that pickle and dill output the same bytes
"""
import pickle

import nose

from joblib.test.common import dill, with_dill, with_py3


def global_func():
    pass


@with_py3
@with_dill
def test_dumps_eq():
    # Test that dill and pickle produce the same results
    nose.tools.assert_equal(dill.dumps(1), pickle.dumps(1))
    nose.tools.assert_equal(dill.dumps({'a': 0, 'b': 1}), pickle.dumps({'a': 0, 'b': 1}))
    nose.tools.assert_equal(dill.dumps(global_func), pickle.dumps(global_func))
