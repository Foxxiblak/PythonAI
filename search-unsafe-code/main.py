from api import get_response

if __name__ == '__main__':
    response = get_response()
    print(response)
    #sensitive_json = search_sensitive_data(response)
    #print(f'sensitive_json: {sensitive_json}')