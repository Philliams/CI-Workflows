from src.subdir import submodule


class TestMain:
    def test_dummy_function(self):
        # Prepare
        a = 1
        b = 2
        c = 3

        expected_res = a * b * c

        # Run
        res = submodule.dummy_function(a, b, c)

        # Assert
        assert res == expected_res
