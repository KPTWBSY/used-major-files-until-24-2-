const boxes=document.querySelectorAll('.box')

window.addEventListener('scroll',checkBoxes)

checkBoxes()

function checkBoxes(){
    const triggerBottom=window.innerHeight / 5 * 4

    boxes.forEach(box=>{
        const boxTop=box.getBoundingClientRect().top /* 개별 박스 맨 위 위치 받아오기.*/

        if(boxTop<triggerBottom){
            box.classList.add('show')
        }
        else{
            box.classList.remove('show')
        }
    })
}