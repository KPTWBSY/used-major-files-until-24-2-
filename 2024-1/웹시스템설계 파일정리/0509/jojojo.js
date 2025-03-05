const audioContainer=document.querySelector('#audioContainer');
const playBtn=document.querySelector('.js-playBtn');
const stopBtn=document.querySelector('.js-stopBtn');

function playAudio(){
    audioContainer.volume=0.2;
    audioContainer.loop=true;
    audioContainer.play();
}

function loadAudio(){
    const source=document.querySelector('#auDIOsource');
    source.src='za-warudo-stop-time-sound.mp3';
    audioContainer.load();
    playAudio();
}

function stopAudio(){
    audioContainer.pause();
}




playBtn.addEventListener('click',loadAudio);
stopBtn.addEventListener('click',stopAudio);

