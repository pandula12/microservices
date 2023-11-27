def format_result(request):
    # get data from POST request
    data = request
    result = data.get('addition_result')

    # format the result into the required JSON format
    jsonString = '{"result": ' + str(result) + '}'

    # any more desired formatting could go here

    # create a response object
    response = [jsonString, 200, {'X-Custom-Header': 'custom-value'}, 'application/json; charset=utf-8']
    
    # return the result
    return response