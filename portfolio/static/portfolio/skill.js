$(document).ready(function(){
var skillset = {
"languages": [
    {
      "name": "Java",
      "skill": 5
    },
    {
      "name": "Python",
      "skill": 5
    },
    {
      "name": "SQL",
      "skill": 4
    },
    {
      "name": "HTML",
      "skill": 2
    },
    {
      "name": "C++",
      "skill": 3
    },
  ],
"frameworks": [
    {
      "name": "Spring Boot/MVC",
      "skill": 5
    },
    {
      "name": "Django",
      "skill": 4
    },
    {
      "name": "Flask",
      "skill": 3
    },
    {
      "name": "Hibernate",
      "skill": 3
    },
  ],
"databases": [
    {
      "name": "MongoDB",
      "skill": 3
    },
    {
      "name": "MySql",
      "skill": 4
    },
],

"os": [
    {
      "name": "Windows",
      "skill": 5
    },
    {
      "name": "Linux",
      "skill": 4
    },
    ],
		"tools": [
		    {
		      "name": "Eclipse",
		      "skill": 5
		    },
		    {
		      "name": "Postman",
		      "skill": 4
		    },
		    {
		      "name": "Docker",
		      "skill": 3
		    },
		    {
		      "name": "Git,GitHub",
		      "skill": 4
		    },
		    {
		      "name": "PyCharm",
		      "skill": 4
		    },
		    {
		      "name": "Tomcat",
		      "skill": 3
		    },
		     {
		      "name": "Android Studio",
		      "skill": 3
		    },

  ]
}



for(var i in skillset.languages){
   var percent=(skillset.languages[i].skill*100)/5
  var str='<div class="skillbar-container"><div class="skillbar" style="background: #2ecc71;" data-percent="'+percent+'%"><li>'+skillset.languages[i].name+'</div></div></li>';
   $(str).appendTo($('.languages'));
}

for(var i in skillset.frameworks){
   var percent=(skillset.frameworks[i].skill*100)/5
  var str='<div class="skillbar-container"><div class="skillbar" style="background: #2ecc71;" data-percent="'+percent+'%"><li>'+skillset.frameworks[i].name+'</div></div></li>';
   $(str).appendTo($('.frameworks'));
}
  for(var i in skillset.databases){
   var percent=(skillset.databases[i].skill*100)/5
  var str='<div class="skillbar-container"><div class="skillbar" style="background: #2ecc71;" data-percent="'+percent+'%"><li>'+skillset.databases[i].name+'</div></div></li>';
   $(str).appendTo($('.databases'));
}
    for(var i in skillset.os){
   var percent=(skillset.os[i].skill*100)/5
  var str='<div class="skillbar-container"><div class="skillbar" style="background: #2ecc71;" data-percent="'+percent+'%"><li>'+skillset.os[i].name+'</div></div></li>';
   $(str).appendTo($('.os'));
}

for(var i in skillset.tools){
var percent=(skillset.tools[i].skill*100)/5
var str='<div class="skillbar-container"><div class="skillbar" style="background: #2ecc71;" data-percent="'+percent+'%"><li>'+skillset.tools[i].name+'</div></div></li>';
$(str).appendTo($('.tools'));
}
  $('.skillbar').each(function(){
	$(this).animate({
		width:$(this).attr('data-percent')
	},2000);
});
})