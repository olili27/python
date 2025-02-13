@app.route('/downloadCRBTemplate',methods=['POST'])
def downloadCRBTemplate():
    payload = request.get_json()

    paramValidation = kisa_utils.structures.validator.validate(payload, {"fileId": str, "userId": str, "institutionId": str})

    if not paramValidation["status"]: return jsonify(paramValidation)

    downloadResponse = institution.downloadCRBTemplate(payload["userId"], payload["institutionId"], payload["fileId"])

    if not downloadResponse["status"]: return jsonify(downloadResponse)

    # do whatever you want with the fileId and return its contents and the file name
    with open(downloadResponse["outputFile"],'rb') as fin:
        data = fin.read()
        import base64
        b64Data = base64.b64encode(data).decode('utf-8')

        return jsonify({
            'status':True, 
            'log':'', 
            'file':{
                'name':downloadResponse["outputFile"].split("/")[-1],
                'b64Data':b64Data,
            }
        })
        