import pytest
import pushover
import responses

# Test parameters
status_codes = {'0', '1'}
priorities = {'lowest', 'low', 'normal', 'high'}


@pytest.fixture(scope="function")
def pushover_client(token):
    return pushover.Client(token, 'user')


def test_get_url(pushover_client):
    assert pushover_client.get_url() == 'https://api.pushover.net/1/messages.json'


@responses.activate
@pytest.mark.parametrize("status_code", status_codes)
def test_send_message(pushover_client, status_code):
    # Prepare the response
    url = pushover_client.get_url()
    responses.add(responses.POST, url, json={'status': status_code, 'request': 'xxx'}, status=200)

    # Run the test
    data = pushover_client.message('test').json()
    assert data['status'] == status_code


@responses.activate
def test_send_empty_message(pushover_client):
    with pytest.raises(TypeError):
        pushover_client.message()


@responses.activate
@pytest.mark.parametrize("priority", priorities)
def test_send_empty_message(pushover_client, priority):
    # Prepare the response
    url = pushover_client.get_url()
    responses.add(responses.POST, url, json={'status': 1, 'request': 'xxx'}, status=200)

    # Run the test
    data = pushover_client.message('test', priority=priority).json()
    assert data['status'] == 1
    with pytest.raises(TypeError):
        pushover_client.message('test', priority='invalid priority')


def test_different_sounds(pushover_client):
    # Prepare the response
    url = pushover_client.get_url()
    responses.add(responses.POST, url, json={'status': 1, 'request': 'xxx'}, status=200)

    # Run the test
    sounds = pushover_client.get_sounds()
    for i in range(2):
        pushover_client.message('test', sound=list(sounds.keys())[i])
    with pytest.raises(TypeError):
        pushover_client.message('test', sound='invalid sound')

