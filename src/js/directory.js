
/*
	Written By: Alex Jaeger 5/5/2014

	Purpose: To control the file directory on directory.html
	Linked Files: directory.html
*/

/*
	<div class="file">
		<a class="file-link" href="#" onclick=""><i class="fa fa-square-o file-icon"></i></a>
		<label class="filename">Backend.py</label>
	</div>
*/

file_id=0;

var selectedFiles=[];
var files=[];

function addFileListing(ul_ID, li_CLASS) {
	$("#"+ul_ID).append('<li class="directory-listing" data-id='+file_id+'><div class="file"><a class="file-link" href="#" onclick="selectFileListing('+file_id+')"><i class="fa fa-square-o file-icon"></i></a><label class="filename">Backend.py</label></div></li>');
	file_id+=1;
}

function deleteFileListing(file_ID) {
	var li=document.querySelectorAll(""+file_ID);
	alert(li);
}

function selectFileListing(file_ID) {
	var selectedFile=document.getElementsByTagName('li')[file_ID];
	var icon=selectedFile.getElementsByTagName('i')[0];

	if(icon.className=="fa fa-square-o file-icon") {
		icon.className="fa fa-check-square-o file-icon";
	}
	
	else {
		icon.className="fa fa-square-o file-icon";
	}
}