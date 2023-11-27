from mkslides.utils import read_yaml


def test_read_yaml():
    _configs = read_yaml("tests/test_configs.yml")
    assert isinstance(
        _configs, dict
    ), f"Test configs file is of type {type(_configs)}; should result in a dictionary."
