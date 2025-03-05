const progress=document.getElementById('progress')
const prev=document.getElementById('prev')
const next=document.getElementById('next')
const circles=document.querySelectorAll('.circle')

let currentActive=1

next.addEventListener('click',()=>{
    currentActive++

    if(currentActive>circles.length){
        currentActive=circles.length
    }

    update()
})

prev.addEventListener('click',()=>{
    currentActive--

    if(currentActive<1){
        currentActive=1
    }

    update()
})

function update(){
    circles.forEach((circle,idx /*idx:인덱스 값 받아옴? */)=>{
        if(idx < currentActive){
            circle.classList.add('active')
        }
        else{
            circle.classList.remove('active')
        }
    })

    const actives=document.querySelectorAll('.active')

    progress.style.width=(actives.length-1)/(circles.length-1)*100+'%'

    if(currentActive===1){
        prev.disabled=true
    }
    else if(currentActive===circles.length){
        next.disabled=true
    }
    else{
        prev.disabled=false
        next.disabled=false
    }

    /*처음에 next 한번 누름
    >> currentActive=2, update()에서 원 1, 2번에 active.
    progress.style.width=33.3%
    
    prev 누름
    >> currentActive=1, update()에서 원 1번(인덱스 0)에 active.
    progress.style.width=0%

    width 0 상태에서 next 세번
    >>currentActive=4, update에서 원 1, 2, 3,4번에 active
    width=100%

    width=100% 상태에서 prev 한번
    >>currentActive=3, update에서 원 1,2,3번에 active
    width=66%(왼쪽으로 줄어듦)

    */
}

