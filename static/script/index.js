after= (_) => {
    parent.window.location.reload();
  }

  var url = "{% url 'statuslike' %}" 

function update(eno){
    var data = {'eno': eno};
    $.post('statuslike/', data, function(returnedData){
        console.log(returnedData);
        after()
    });
}

function toggle(id,likebtn){
    var btn=document.getElementById(id);
    if(btn.classList.contains('black')){
        btn.classList.remove('black');
        btn.classList.add('red');
        // update(likebtn)
}
    else{
        btn.classList.remove('red');
        btn.classList.add('black');
    }
}

document.addEventListener('DOMContentLoaded', function() {
    
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems);
    instances.open();
  });
