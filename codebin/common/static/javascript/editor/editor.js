function SaveCode()
{

}

function SendAjaxRequest(resultControl, isAsync, destination, message)
{
	var xmlHttp = new XMLHttpRequest();
	xmlHttp.onreadystatechange = function()
	{
		if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
		{
			resultControl(xmlHttp.responseText);
		}
		else if (xmlHttp.status == 404)
		{
			resultControl("Error");
		}
	}
	xmlHttp.open("POST", destination, isAsync);
	xmlHttp.setRequestHeader("Content-Type", "applicaiton/x-www-form-urlencoded");
	xmlHttp.send(message);
}
