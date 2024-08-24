
    function updateFileName() {
        const fileInput = document.getElementById('file');
        const fileInfo = document.getElementById('file-info');
        const fileName = fileInput.files.length > 0 ? fileInput.files[0].name : 'No file chosen';
        fileInfo.textContent = `Selected file: ${fileName}`;
    }

