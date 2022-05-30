setTimeout(function () {
    let messages = document.getElementById("msg");
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 3000);


function clear() {
    var textarea = document.getElementById("id_body");
    textarea.reset();
}