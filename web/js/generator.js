
    function generate(form) {

        var filename = form.filename.value
        var filetype = form.filetype.value
        var valuefrom = form.fromValue.value
        var valueto = form.toValue.value
        
        if (filename == "") filename = "result"

        console.log(filename, filetype, valuefrom, valueto)
        
        downloadBlob("../output/result" + filetype, filename)
 
    }


    function downloadBlob(blob, filename) {
        var a = document.createElement('a');
        a.download = filename;
        a.href = blob;
        document.body.appendChild(a);
        a.click();
        a.remove();
    }