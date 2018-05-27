import pytest
class Test_01:

    @pytest.mark.parametrize("a,b",[(60,61),(59,70),(59,58),(80,85)])
    def test_001(self,a,b):
        c = a + b
        assert c >= 120 and a >= 60 

