from src import main

class TestMain:

    def test_dummy_function(self):
        # Prepare
        a = 1
        b = 2

        expected_res = 1

        # Run
        res = main.dummy_function(a, b)

        # Assert
        assert res == expected_res