function SendAjaxRequest(resultControl, isAsync, destination, headers, message)
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
	for (var index = 0; index < headers.length; index++)
	{
		xmlHttp.setRequestHeader(headers[index][0], headers[index][1]);
	}
	xmlHttp.send(message);
}
