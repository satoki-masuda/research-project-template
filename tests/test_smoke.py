def test_package_import() -> None:
    import src

    assert src.__doc__
