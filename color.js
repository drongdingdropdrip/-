
                function hello(){
                    var d= document.querySelector('body');
        var f = document.querySelectorAll('a');
        var i = 0;
        if(this.value === '밤'){
         d.style.backgroundColor = 'black';
            d.style.color = 'white';
            while(i < f.length){
                f[i].style.color = 'powderblue';
                i = i + 1;
            }
            this.value = '낮';
        }
        else{
            d.style.backgroundColor = 'white';
            d.style.color = 'black';
            while(i < f.length){
                f[i].style.color = 'blue';
                i = i + 1;
            }
            this.value = '밤';
        }
    }           