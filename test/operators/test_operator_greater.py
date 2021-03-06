from s2e2.error import ExpressionError
from s2e2.operators.operator_greater import OperatorGreater

import pytest


class TestOperatorGreater:

    def setup_class(self):
        self.operator = OperatorGreater()


    def teardown_class(self):
        self.operator = None


    def test_positive_good_arguments_stack_size(self):
        stack = ['string1', 'string2']
        self.operator.invoke(stack)
        assert len(stack) == 1


    def test_positive_good_arguments_result_type(self):
        stack = ['string1', 'string2']
        self.operator.invoke(stack)
        assert isinstance(stack[0], bool)


    def test_positive_equal_strings_result_value(self):
        stack = ['string1', 'string1']
        self.operator.invoke(stack)
        assert not stack[0]


    def test_positive_equal_integers_result_value(self):
        stack = [5001, 5001]
        self.operator.invoke(stack)
        assert not stack[0]


    def test_positive_first_argument_greater_result_value(self):
        stack = ['string2', 'string1']
        self.operator.invoke(stack)
        assert stack[0]


    def test_positive_second_argument_greater_result_value(self):
        stack = [5, 55]
        self.operator.invoke(stack)
        assert not stack[0]


    def test_positive_more_arguments_stack_size(self):
        stack = ['string1', 'string2', 'string3']
        self.operator.invoke(stack)
        assert len(stack) == 2


    def test_negative_fewer_arguments(self):
        stack = ['string']
        with pytest.raises(ExpressionError) as ex:
            self.operator.invoke(stack)
        assert 'Not enough arguments' in str(ex.value)


    def test_negative_first_argument_none(self):
        stack = [None, 'string']
        with pytest.raises(ExpressionError) as ex:
            self.operator.invoke(stack)
        assert 'Invalid arguments' in str(ex.value)


    def test_negative_second_argument_none(self):
        stack = ['string', None]
        with pytest.raises(ExpressionError) as ex:
            self.operator.invoke(stack)
        assert 'Invalid arguments' in str(ex.value)


    def test_negative_both_arguments_none(self):
        stack = [None, None]
        with pytest.raises(ExpressionError) as ex:
            self.operator.invoke(stack)
        assert 'Invalid arguments' in str(ex.value)


    def test_negative_arguments_of_different_types(self):
        stack = ['string', 55]
        with pytest.raises(ExpressionError) as ex:
            self.operator.invoke(stack)
        assert 'Invalid arguments' in str(ex.value)
