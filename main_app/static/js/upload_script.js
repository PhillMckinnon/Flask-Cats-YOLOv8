document.getElementById('upload-form').onsubmit = async (event) => {
    event.preventDefault();
    try {
        const formData = new FormData(event.target);
        const response = await fetch('/getcats/', { method: 'POST', body: formData });
        if (!response.ok) throw new Error('Failed to process image');
        const blob = await response.blob();
        const url = URL.createObjectURL(blob);
        document.getElementById('output-image').src = url;
        document.getElementById('download-link').href = url;
    } catch (error) {
        console.error(error.message);
    }
};