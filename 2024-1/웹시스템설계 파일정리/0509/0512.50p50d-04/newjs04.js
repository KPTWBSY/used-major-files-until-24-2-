const search=document.querySelector('.search')
const btn=document.querySelector('.btn')
const input=document.querySelector('.input')

btn.addEventListener('click',()=>{
    search.classList.toggle('active') /*클래스가 존재한다면 클래스를 제거, 존재하지 않는다면 추가하는 메소드. */
    input.focus()
})

