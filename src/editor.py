import cgi

print "Content-Type: text/html\n"

form = cgi.FieldStorage()


print """
<!DOCTYPE html>
<html lang="en">

<head>
    <title>CodeBin</title>
    <link rel="stylesheet" type="text/css" href="./css/editor.css"/>

    <link rel="stylesheet" rel="stylesheet" type="text/css" media="screen" href="http://openfontlibrary.org/face/hans-kendrick"/>
    <link rel="stylesheet" href="./bin/icons/font-awesome-4.0.3/css/font-awesome.min.css"/>


    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.0/jquery.min.js" type="text/javascript"></script> 
    <script src="./js/skulpt.min.js" type="text/javascript"></script> 
    <script src="./js/skulpt-stdlib.js" type="text/javascript"></script>
    <script type="text/javascript">

    function Sound(source,volume,loop)
    {
      this.source=source;
      this.volume=volume;
      this.loop=loop;
      var son;
      this.son=son;
      this.finish=false;
      this.stop=function()
      {
          document.body.removeChild(this.son);
      }
      this.start=function()
      {
          if(this.finish)return false;
          this.son=document.createElement("embed");
          this.son.setAttribute("src",this.source);
          this.son.setAttribute("hidden","true");
          this.son.setAttribute("volume",this.volume);
          this.son.setAttribute("autostart","true");
          this.son.setAttribute("loop",this.loop);
          document.body.appendChild(this.son);
      }
      this.remove=function()
      {
          document.body.removeChild(this.son);
          this.finish=true;
      }
      this.init=function(volume,loop)
      {
          this.finish=false;
          this.volume=volume;
          this.loop=loop;
      }
    }

      //Konami Code Implementation
      if (window.addEventListener) {
        var keys = [];
        var konami = "38,38,40,40,37,39,37,39,66,65";
        var r_konami = "65,66,39,37,39,37,40,40,38,38";
        var index=0;

        window.addEventListener("keydown", function(e){
            keys.push(e.keyCode);
            
            if (keys.toString().indexOf(konami) >= 0) {
              var bg=["./bin/img/bunny-fail.gif","./bin/img/tab.gif","./bin/img/laughing.gif","./bin/img/beer.gif","./bin/img/ugh.gif","./bin/img/energy.gif"];             
              var bg_file=bg[index];

              document.body.style.backgroundImage="url("+bg_file+")";
              
              if(index>5) {
                index=0;
              }

              else {
                index++;
              }

              keys = [];
            };

        }, true);
      };


      function startRickRoll() {
        alert("Turn up your volume, You just got RickRolled!");
        var rickroll = new Sound("bin/mp3/rickroll.mp3",100,true);
        rickroll.start();
      }
  function loadtext()
  {
"""
try:
  print """
  var xmlhttp=new XMLHttpRequest();
  xmlhttp.onreadystatechange=function()
  {
    if (xmlhttp.readyState==4 && xmlhttp.status==200)
    {
      var text=xmlhttp.responseText;
      alert(text);
      editor.getSession().setValue(text);
    }
    else if (xmlhttp.status==404)
    {
      editor.getSession().setValue('An error occured.');
    }
  }
  xmlhttp.open("POST","backend.py",true);
  xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
  xmlhttp.send("pick=1&hash="+'%s');
  """%(str(form['hash'].value))
except:
  print """editor.getSession().setValue('print \"Hello World\"');"""
print """
}
    </script> 
</head>

<body onload="loadtext()">

  <script type="text/javascript"> 
    // output functions are configurable.  This one just appends some text
    // to a pre element.
    function outf(text) { 
        var mypre = document.getElementById("output"); 
        mypre.innerHTML = mypre.innerHTML + text; 
    } 
    function builtinRead(x) {
        if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][x] === undefined)
                throw "File not found: '" + x + "'";
        return Sk.builtinFiles["files"][x];
    }
     
    // Here's everything you need to run a python program in skulpt
    // grab the code from your textarea
    // get a reference to your pre element for output
    // configure the output function
    // call Sk.importMainWithBody()
    function runit() { 
  	var prog = editor.getSession().getValue(); 
  	var mypre = document.getElementById("output"); 
   	mypre.innerHTML = ''; 
  	Sk.canvas = "mycanvas";
  	Sk.pre = "output";
  	Sk.configure({output:outf, read:builtinRead}); 
  	eval(Sk.importMainWithBody("<stdin>",false,prog));   
  } 
    function savetext()
    {
	    var xmlhttp=new XMLHttpRequest();
"""
try:
	print """
      xmlhttp.open("POST","backend.py",true);
      xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
      xmlhttp.send("pick=2&code="+editor.getSession().getValue()+"&hash=%s");
  """%(str(form['hash'].value))

except:
	print """
      var newHash="";
      xmlhttp.onreadystatechange=function()
      {
        if (xmlhttp.readyState==4 && xmlhttp.status==200)
        {
          newHash=xmlhttp.responseText;  
          window.location=document.URL+"?hash="+newHash;
        }
        else if (xmlhttp.status==404)
        {
          editor.getSession().setValue("An error occured.");
        }
      }
      xmlhttp.open("POST","backend.py",true);
      xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
    	xmlhttp.send("pick=3&code="+editor.getSession().getValue());
	"""
print """
    }
  </script> 
  <div id="header-content">
    <a class="easter-egg" href="#" onclick="startRickRoll()"><h1 id="logo">CodeBin</h1></a>

  </div>

  <div id="body-content">
      <form id="body-form">  
        <div id="editor"></div>
        <div id="output">
          <canvas id="mycanvas" ></mycanvas> 
        </div>
        <button id="run-button" type="button" onclick="savetext(); runit();">Run</button> 
      </form>  
  </div>

  <div id="footer-content">
    <p>CodeBin Copyright 2014 Written By <a class="easter-egg" href="http://bit.ly/1eUpyT1">Alex Jaeger</a> and <a class="easter-egg" href="./bin/img/cat.jpg">Dylan Johnson</a>. Documentation and Support provided by the <a class="easter-egg" href="./bin/img/california-condor.jpg">Condor</a></p>
  </div>

  <script src="./bin/libraries/ace-builds-master/src-noconflict/ace.js" type="text/javascript" charset="utf-8"></script>
  <script>
      var editor=ace.edit("editor");
      editor.setTheme("ace/theme/tomorrow_night");
      editor.getSession().setMode("ace/mode/python");
      editor.setFontSize(12);
 	</script>	

</body>

</html>
"""