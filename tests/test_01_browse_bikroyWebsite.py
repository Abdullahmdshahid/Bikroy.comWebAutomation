from tests.base_test import BaseTestClass


class Test(BaseTestClass):

    # checking is it correct url or not
    def test_01(self):
        assert "https://bikroy.com/" == self.driver.current_url
