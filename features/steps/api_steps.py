from behave import given, then
from utils.api_utils import make_get_request

@given('I make a GET request to "{endpoint}"')
def step_make_get_request(context, endpoint):
    context.response = make_get_request(endpoint)

@then('the response status code should be {status_code:d}')
def step_check_status_code(context, status_code):
    assert context.response.status_code == status_code, f"Expected status code {status_code}, but got {context.response.status_code}"
