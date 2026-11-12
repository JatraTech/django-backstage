function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) {
    return parts.pop().split(";").shift();
  }
  return "";
}

function tinymceImageUploadHandler(blobInfo, progress) {
  return new Promise((resolve, reject) => {
    const xhr = new XMLHttpRequest();
    xhr.withCredentials = true;
    xhr.open("POST", "/admin/tinymce/upload/");
    xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));

    xhr.upload.onprogress = (event) => {
      if (event.lengthComputable) {
        progress((event.loaded / event.total) * 100);
      }
    };

    xhr.onload = () => {
      if (xhr.status < 200 || xhr.status >= 300) {
        reject(`Image upload failed (${xhr.status})`);
        return;
      }

      try {
        const json = JSON.parse(xhr.responseText);
        if (!json.location) {
          reject("Invalid upload response.");
          return;
        }
        resolve(json.location);
      } catch {
        reject("Invalid upload response.");
      }
    };

    xhr.onerror = () => reject("Image upload failed.");

    const formData = new FormData();
    formData.append("file", blobInfo.blob(), blobInfo.filename());
    xhr.send(formData);
  });
}
