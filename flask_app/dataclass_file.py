# dataclass_file.py creates data classes

@dataclass
@dataclass_json
class CreateUserSimsRequest:
    user_handle: int



@dataclass
@dataclass_json
class CreateUserSimsResponse:
    user_handle: int
    nearest_users: dict

OPERATION_CREATE_USERSIMS: str: 'create-usersims'
@app.route(f'/{OPERATION_CREATE_USERSIMS}', methods=['POST'])
def create_usersims():
    payload = request.get_json()
    logging.info(f"Incoming payload for {OPERATION_CREATE_PERSON}: {payload}")
    user_sims = CreateUserSimsRequest.from_json(payload)


# To generate a corresponding API Definition, enter:

spec = {}

generate_operation(path=OPERATION_CREATE_USERSIMS,
        request_schema=CreateUserSimsRequest.schema(),
        request_schema_name=CreateUserSimsResponse.schema(),
        response_schema_name=CreateUserSimsResponse.__name__,
        spec=spec)

spec_dict = spec.to_dict()




