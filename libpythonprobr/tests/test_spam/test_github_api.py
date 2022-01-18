from unittest.mock import Mock

from libpythonprobr import github_api


def test_buscar_avatar():
    resp_mock = Mock()
    resp_mock.json.return_value = {
        'login': 'Moronicwb', 'id': 40072506,
        'avatar_url': 'https://avatars.githubusercontent.com/u/40072506?v=4'
    }
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.buscar_avatar('Moronicwb')
    assert 'https://avatars.githubusercontent.com/u/40072506?v=4' == url
