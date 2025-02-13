function getCRBTemplate(fileId) {
  // fileId: 'CAB', 'CBA', 'PI', 'IB', 'CMC', 'all';

  downloadCRBTemplate(
    {
      userId: "",
      endpoint: "",
      fileId: fileId,
    },
    isLoading
  );
}

function downloadCRBTemplate(details, isLoading) {
  // extract data from the `details` objects

  if (!details || !details.endpoint || !details.userId || !details.fileId) {
    alert("invalid `details` object given");
    return;
  }

  const endpoint = details.endpoint; // "downloadFile"; // get this from where it should be
  const payload = {
    userId: details.userId, // userId from wherever it is
    fileId: details.fileId,
  };

  // start 'loanding' animation
  // ...
  isLoading ? isLoading(true) : null;

  fetch(endpoint, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json",
    },
    body: JSON.stringify(payload),
  })
    .then((response) => {
      // stop 'loanding' animation
      // ...

      if (!response.ok) {
        alert("failed to download file. server/network error");
        isLoading ? isLoading(false) : null;
        raise("x");
      }
      return response.json();
    })
    .then(async (response) => {
      if (!response.status) {
        alert(`ERROR: ${response.log}`);
        isLoading ? isLoading(false) : null;
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
      var blob = new Blob([arrayBuffer], { type: "application/octet-stream" });

      // Create link element
      var link = document.createElement("a");
      link.href = window.URL.createObjectURL(blob);

      // Set the filename (optional)
      link.download = fileData.name;

      isLoading ? isLoading(false) : null;

      // Trigger the download
      link.click();
    });
}
