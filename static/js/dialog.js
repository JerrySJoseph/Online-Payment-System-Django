;(function(){
    const dialogModal=new bootstrap.Modal(document.getElementById('modal'))
   
    document.body.addEventListener('htmx:afterSwap',function(e){
        
        if(e.detail.target.id==='dialog'){
            dialogModal.show()          
        }
    })
})()