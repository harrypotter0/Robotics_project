var n; // world size
var measurement = [];
var motion = []
var phit = 0.8;
var pmiss = 0.2;
var p = [];
var pexact = 0.8;
var pover = 0.1;
var punder=0.1;
world_array = [];
graph_data = [];

var sense_data = function(z){
var sum= 0.0;
  for(var i=0;i<n;++i)
  {
    if(world_array[i]==z)
      p[i]=p[i]*phit;
    else
      p[i]=p[i]*pmiss;
    sum+=p[i];
  }
  console.log("Sum"+sum);
  
  for(var i=0;i<n;++i)
  {  p[i]/=sum; }
  
  console.log(p);
  

}

var move = function(z)
{
  var ss,len,i1,i2,i3;
  len = parseInt(n);
  var q = [];
  for(var i=0;i<n;++i)
  {
     ss=0.0;
     i1 = i-z+len;
     i2 = i-z-1+len;
     i3 = i-z+1+len;
     i1=i1%len;
     i2=i2%len;
     i3=i3%len;
    
     ss=ss+p[i1]*pexact;
     ss=ss+p[i2]*pover;
     ss=ss+p[i3]*punder;
     q.push(ss);
  }
  p=q;

  console.log(p);

}
var update_world = function(){

  measurement = document.getElementById("measure").value.split(',');
  

  console.log(measurement);

  motion = document.getElementById("motion").value.split(',');
  for(var i=0;i<motion.length;i++){
     motion[i] = parseInt(motion[i]);
  }

  console.log(motion);

  world_array=[];
  for(var i=0;i<n;i++){
      var color = document.getElementById('world').children[i].className;
      if(color=="world-cell red"){
        world_array.push('R');
      }
      else{
        world_array.push('G');
      }
  }
document.getElementById('message_one').innerHTML="Actual World : "+ world_array;


}


var generate_world= function(){
	//console.log("hey");
	n = document.getElementById("no_of_cells").value;
	console.log(n);


    world = document.getElementById('world');
    world.innerHTML = "";
  
  for (i=0;i<n;i++){
    console.log("Hre");
    cell = document.getElementsByClassName('world-cell')[0];
    var new_cell = document.createElement('div');
    new_cell.className="world-cell";
    new_cell.className +=" red";
    
    new_cell.addEventListener('click',function(){
      if(this.className="world-cell red")
        { this.className = "world-cell green";}
      else if(this.className="world-cell green"){
        this.className="world-cell red";
      }
    });
   document.getElementById('world').appendChild(new_cell);
    p.push(1.0/n);
   
  }
}

var final_data = function()
{
   var len = measurement.length;
  for(var i=0;i<len;++i)
  {
    sense_data(measurement[i]);
    move(motion[i]);
  }
  update_graph();
}
var update_graph=function(){

 for(i=0;i<n;i++){
      graph_data.push({"x":i+1,"y":p[i]})
  }

var data = {
  "xScale": "ordinal",
  "yScale": "linear",
  "main": [
    {
      "className": ".pizza",
      "data":graph_data,
    }
  ]
};
var myChart = new xChart('bar', data, '#example1');
}