
if __name__=='__main__':
    from flask import Flask, request, jsonify
    app = Flask(__name__)

    @app.route('/downloadCRBTemplate',methods=['POST'])
    def downloadCRBTemplate():
        userId = request.json['userId']
        fileId = request.json['fileId']

        # do whatever you want with the fileId and return its contents and the file name
        fileName = 'p.py'
        with open(fileName,'rb') as fin:
            data = fin.read()
            import base64
            b64Data = base64.b64encode(data).decode('utf-8')

            return jsonify({
                'status':True, 
                'log':'', 
                'file':{
                    'name':fileName,
                    'b64Data':b64Data,
                }
            })

    @app.route('/',methods=['GET','POST'])
    def index():
        return '''
        <html>
            <head>
                <title>File Download Test</title>
                <script>
                    function downloadFile(details){
                        // extract data from the `details` objects

                        const endpoint = 'downloadFile'; // get this from where it should be
                        const payload = {
                            userId: '', // userId from wherever it is
                            fileId: details.fileId, 
                        };

                        // start 'loanding' animation
                        fetch(endpoint, {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json',
                                'Accept': 'application/json',
                            },
                            body: JSON.stringify(payload)
                        })
                        .then(response => {
                            // stop 'loanding' animation

                            if(!response.ok){
                                alert('failed to download file. server/network error');
                                raise('x');
                            }
                            return response.json();
                        })
                        .then(async response => {
                            if(!response.status){
                                alert(`ERROR: ${response.log}`);
                                return;
                            }
                            const fileData = response.file;

                            // Convert base64 to binary
                            var binaryData = await atob(fileData.b64Data);

                            // Convert binary to ArrayBuffer
                            var arrayBuffer = new ArrayBuffer(binaryData.length);
                            var view = new Uint8Array(arrayBuffer);
                            for (var i = 0; i < binaryData.length; i++) {
                                view[i] = binaryData.charCodeAt(i);
                            }

                            // Create blob from ArrayBuffer
                            var blob = new Blob([arrayBuffer], { type: 'application/octet-stream' });

                            // Create link element
                            var link = document.createElement('a');
                            link.href = window.URL.createObjectURL(blob);

                            // Set the filename (optional)
                            link.download = fileData.name;

                            // Trigger the download
                            link.click();
                            
                        })
                    }
                </script>
            </head>
            <body>
                <button onclick="downloadFile({fileId:'CAB'})">download file</button>
            </body>
        </html>
        '''

    app.run('0.0.0.0',7000,threaded=1, debug=1)