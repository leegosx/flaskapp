// static/js/app.js
function updateFileName() {
    const fileInput = document.getElementById('fileInput');
    const fileNameLabel = document.getElementById('fileNameLabel');
    if (fileInput.files.length > 0) {
        fileNameLabel.textContent = "Uploaded file: " + fileInput.files[0].name;
    } else {
        fileNameLabel.textContent = "No file chosen";
    }
}

function toggleFileContent() {
    const fileContent = document.getElementById('fileContent');
    if (fileContent.style.display === 'none' || fileContent.style.display === '') {
        fileContent.style.display = 'block';
    } else {
        fileContent.style.display = 'none';
    }
}
