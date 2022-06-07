import pytest


@pytest.mark.usefixtures("setup")
class Test:

    # checking is it correct url or notgit
    def test_01(self):
        assert "https://bikroy.com/bn" == self.driver.current_url
