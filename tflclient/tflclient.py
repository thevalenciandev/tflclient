import json
import requests
from types import SimpleNamespace


API_BASE_URL = 'https://api.tfl.gov.uk'
LINE_URL = API_BASE_URL + '/Line'
LINE_DISRUPCAT_ENDPOINT = LINE_URL + '/Meta/DisruptionCategories'
LINE_SEVERITYCODES_ENDPOINT = LINE_URL + '/Meta/Severity'
LINE_MODE_ENDPOINT = LINE_URL + '/Mode/{}'
LINE_MODE_STATUS_ENDPOINT = LINE_MODE_ENDPOINT + '/Status'

HEADERS = {"Cache-Control": "no-cache"}


def get_disruption_categories():
    """Gets a list of valid disruption categories

    """
    categories = requests.get(LINE_DISRUPCAT_ENDPOINT,
                              headers=HEADERS)

    return _to_object_or_throw_with_msg(categories, 'disruption categories')


def get_lines_for_modes(*modes):
    r"""Gets lines that serve the given modes

    :param \*modes: List of modes to filter by. eg. tube, overground
    """
    lines = requests.get(LINE_MODE_ENDPOINT.format(_comma_separated(modes)),
                         headers=HEADERS)

    return _to_object_or_throw_with_msg(lines, 'lines for {modes}')


def get_severity_codes():
    """Gets a list of valid severity codes

    """
    severities = requests.get(LINE_SEVERITYCODES_ENDPOINT,
                              headers=HEADERS)

    return _to_object_or_throw_with_msg(severities, 'severity codes')


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

    return _to_object_or_throw_with_msg(status, 'status for {modes}')


def get_modes():
    """Gets a list of valid modes. eg. tube, dlr

    """
    modes = requests.get(f'{API_BASE_URL}/Line/Meta/Modes',
                         headers=HEADERS)

    return _to_object_or_throw_with_msg(modes, 'modes')


def _to_object_or_throw_with_msg(response, msg):
    if response.status_code != 200:
        raise Exception(f'Could not get {msg}. Response: {response}')

    return _to_object(response)


def _to_object(result):
    return json.loads(result.content,
                      object_hook=lambda d: SimpleNamespace(**d))


def _comma_separated(obj):
    return ",".join(obj)
