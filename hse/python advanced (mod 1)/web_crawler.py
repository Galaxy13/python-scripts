import json

address_list = []
def recursive_sum_address(key, value, prev_value=''):
    if not isinstance(value, dict) or not value:
        address_list.append(prev_value + str(key))
    for new_key, new_value in value.items():
        recursive_sum_address(new_key, new_value, prev_value + str(key) + '/')

def solve(input_json: str) -> str:
    global address_list
    address_list = []
    addresses = json.loads(input_json)
    for key in addresses:
        recursive_sum_address(key, addresses[key])
    return sorted(address_list)