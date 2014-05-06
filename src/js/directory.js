
/*
	<div class="file"><a class="file-link" href="#" onclick=""><i class="fa fa-edit file-icon"></i></a><label class="filename">Backend.py</label></div>

*/

file_id=0

function addFileListing(ul_ID, li_CLASS) {
	
	$("#"+ul_ID).append('<li class="directory-listing"><div class="file"><a class="file-link" href="#" onclick=""><i class="fa fa-edit file-icon"></i></a><label class="filename">Backend.py</label></div></li>');

	file_id+=1;
}

function deleteFileListing(file_ID) {
	var li=document.querySelectorAll(""+file_ID);
	alert(li);
}