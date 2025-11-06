import app


def test_random_fruit():
    assert "Apple" or "Cherry" or "Orange" in app.random_fruit()
