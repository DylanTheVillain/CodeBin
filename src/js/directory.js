
/*
	Written By: Alex Jaeger 5/5/2014

	Purpose: To control the file directory on directory.html
	Linked Files: directory.html
*/

/*
	<div class="file">
		<a class="file-link" href="#" onclick=""><i class="fa fa-square-o file-icon"></i></a>
		<label class="filename">Backend.py</label>
		<input class="new-filename"type="text" name="filename"/>
	</div>
*/

file_id=0;

var selectedFiles=[];
var files=[];


/*
	Adds a file listing to the ul

	@param ul_ID the id of the ul
	@param li_CLASS the class of the li
*/
function addFileListing(ul_ID, li_CLASS) {
	$("#"+ul_ID).append('<li class="directory-listing" data-id='+file_id+'>\
		<div class="file">\
			<a class="file-link" href="#" onclick="selectFileListing('+file_id+')"><i class="fa fa-square-o file-icon"></i></a>\
				<input class="new-filename"type="text" onKeyPress="return keyEvent(this)" name="filename"/>\
		</div>\
	</li>');

	file_id++;
}

function deleteFileListing() {
	for(var i=0;i<selectedFiles.length;i++) {
		var elem=selectedFiles[i];
		elem.parentNode.removeChild(elem);

		selectedFiles[i]=null;
		file_id--;
	}

	return false;
}

function downloadFileListing() {
	alert("test");
	for(var i=0;i<selectedFiles.length;i++) {
		console.log(i);
	}
}

function selectFileListing(file_ID) {
	var selectedFile=document.getElementsByTagName('li')[file_ID];
	var icon=selectedFile.getElementsByTagName('i')[0];

	if(icon.className=="fa fa-square-o file-icon") {
		icon.className="fa fa-check-square-o file-icon";
		selectedFiles.push(selectedFile);
	} else {
		icon.className="fa fa-square-o file-icon";
	}
}

function keyEvent(e) {
    var keycode;

    if (window.event) 
    	keycode = window.event.keyCode;
    else if (e) 
    	keycode = e.which;
    else 
    	return true;

    if (keycode==13) {
        alert("Enter");
        //myfield.form.submit();
        return false;
    }

    else
        return true;
}