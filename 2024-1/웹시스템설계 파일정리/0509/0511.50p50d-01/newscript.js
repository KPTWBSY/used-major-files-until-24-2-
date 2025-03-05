const panels=document.querySelectorAll('.panel')

panels.forEach(panel=>{
    panel.addEventListener('click',()=>{
        removeActiveClasses()
        panel.classList.add('active') // panel active >> 클래스를 두개 쓰고있는 것. active라는 클래스를 추가하고 제거함에 따라 기능이 실행되도록 함.
    })
})

function removeActiveClasses(){
    panels.forEach(panel=>{
        panel.classList.remove('active')
    })
}

//querySelector()와 querySelectorAll()의 차이
//전자는 선택된 선택자 또는 선택자 그룹과 일치하는 문서 내 첫번째 원소를 반환.
//후자는 선택된 선택자 그룹에 일치하는 도쿠먼트의 엘리먼트 리스트를 나타내는 NodeList를 반환.


//모든 판넬에 판넬을 클릭하면 모든 판넬에서 현재 active 클래스를 제거하고, 
//현재 판넬에 active 클래스를 추가하는 기능 추가.