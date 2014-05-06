
file_id=0

function addFileListing(ul_ID, li_CLASS) {
	var ul=document.getElementById(ul_ID);
	var li=document.createElement("li");

	li.appendChild(document.createTextNode("FOUR"));
	li.setAttribute("class", "li_CLASS");
	li.setAttribute("data-id", ""+file_id);
	ul.appendChild(li);

	file_id+=1;
}

function deleteFileListing(file_ID) {
	var li=document.querySelectorAll(""+file_ID);
	alert(li);
}