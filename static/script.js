function copyToClipboard() {
    var input = document.getElementById("CopyItem");
    
    var clipboard = new ClipboardJS('.btn-copy', {
        text: function() {
            return input.value;
        }
    });

    clipboard.on('success', function(e) {
        alert("Link copied: " + e.text);
    });

    clipboard.on('error', function(e) {
        alert("Copying failed");
    });
}
