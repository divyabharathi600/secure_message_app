document.getElementById('method').addEventListener('change', function () {
    const method = this.value;
    const shiftBox = document.getElementById('shift-container');
    shiftBox.style.display = (method === 'Caesar') ? 'block' : 'none';
});

function encryptMessage() {
    const method = document.getElementById('method').value;
    const message = document.getElementById('message').value;
    const shift = document.getElementById('shift').value;

    fetch('/encrypt', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ method, message, shift })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById('encrypted').textContent = data.encrypted;
        document.getElementById('decrypted').textContent = data.decrypted;
    });
}
