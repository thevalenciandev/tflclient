import json
import requests
from types import SimpleNamespace


API_BASE_URL = 'https://api.tfl.gov.uk'
LINE_MODE_ENDPOINT = API_BASE_URL + '/Line/Mode/{}'
LINE_MODE_STATUS_ENDPOINT = LINE_MODE_ENDPOINT + '/Status'

HEADERS = {"Cache-Control": "no-cache"}


def get_lines_for_modes(*modes):
    r"""Gets lines that serve the given modes

    :param \*modes: List of modes to filter by. eg. tube, overground
    """
    lines = requests.get(LINE_MODE_ENDPOINT.format(_comma_separated(modes)),
                         headers=HEADERS)
    if not lines:
        raise Exception(f'Could not get lines for {modes}')

    return _to_object(lines)


def get_status(*modes, detail=None, severityLevel=None):
    r"""Gets the line status of for all lines for the given modes

    :param \*modes: List of modes to filter by. eg. tube, overground
    :param detail: Include details of the disruptions that are causing the line
        status including the affected stops and routes
    """
    params = {}
    if detail:
        params['detail'] = str(detail).lower()
    if severityLevel:
        params['severityLevel'] = severityLevel

    status = requests.get(LINE_MODE_STATUS_ENDPOINT.format(_comma_separated(modes)),
                          headers=HEADERS,
                          params=params)
    if not status:
        raise Exception(f'Could not get status for {modes}')

    return _to_object(status)


def get_modes():
    """Gets a list of valid modes. eg. tube, dlr

    """
    modes = requests.get(f'{API_BASE_URL}/Line/Meta/Modes',
                         headers=HEADERS)
    if not modes:
        raise Exception('Could not get modes')

    return _to_object(modes)


def _to_object(result):
    return json.loads(result.content,
                      object_hook=lambda d: SimpleNamespace(**d))


def _comma_separated(obj):
    return ",".join(obj)
