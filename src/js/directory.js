
/*
	<div class="file">
		<a class="file-link" href="#" onclick=""><i class="fa fa-edit file-icon"></i></a>
		<label class="filename">Backend.py</label>
	</div>

*/

file_id=0

function addFileListing(ul_ID, li_CLASS) {
	var ul=document.getElementById(ul_ID);
	var li=document.createElement("li");


	var div=document.createElement("div");
		div.setAttribute("class","file");
	var a=document.createElement("a");
		a.setAttribute("class","file-link");
		a.setAttribute("href","#");
		a.setAttribute("onclick","");
	var label=document.createElement("label");
		label.setAttribute("class","filename");
		label.innerHTML="Hello";
		
	div.appendChild(a);
	div.appendChild(label);

	li.appendChild(div);
	li.setAttribute("class", ""+li_CLASS);
	li.setAttribute("data-id", ""+file_id);

	ul.appendChild(li);

	file_id+=1;
}

function deleteFileListing(file_ID) {
	var li=document.querySelectorAll(""+file_ID);
	alert(li);
}