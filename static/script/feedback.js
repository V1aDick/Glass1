let stars = document.querySelectorAll('.star')
let starForm = document.querySelector('.feedback-stars')

let star1 = document.getElementById('Star_1')
let star2 = document.getElementById('Star_2')
let star3 = document.getElementById('Star_3')
let star4 = document.getElementById('Star_4')
let star5 = document.getElementById('Star_5')

stars.forEach(star => {
    star.addEventListener('mouseover', (evt)=>{
        if(evt.target == star1){
            star1.parentNode.classList.add('active')
        }
        else if(evt.target == star2){
            star1.parentNode.classList.add('active')
            star2.parentNode.classList.add('active')
        }
        else if(evt.target == star3){
            star1.parentNode.classList.add('active')
            star2.parentNode.classList.add('active')
            star3.parentNode.classList.add('active')
        }
        else if(evt.target == star4){
            star1.parentNode.classList.add('active')
            star2.parentNode.classList.add('active')
            star3.parentNode.classList.add('active')
            star4.parentNode.classList.add('active')
        }
        else if(evt.target == star5){
            star1.parentNode.classList.add('active')
            star2.parentNode.classList.add('active')
            star3.parentNode.classList.add('active')
            star4.parentNode.classList.add('active')
            star5.parentNode.classList.add('active')
        }
    })
});

starForm.addEventListener('mouseout', (evt)=>{
    stars.forEach(s => {
        s.classList.remove('active')
    });
})