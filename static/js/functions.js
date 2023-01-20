//Typewriter
let skipped = false;

const startJourney = (event) => {
  //HIDE OPTIONS
  document.getElementById("options").style.display = 'none';

  //START TYPEWRITING THE TEXT
  let first = tply.animate(
    document.getElementById("source"),
    document.getElementById("destination")
  );
  let second = tply.animate(
    document.getElementById("source-1"),
    document.getElementById("destination-1")
  );
  setTimeout(
    function() {
      document.querySelector('#destination .cursor').style.display='none';
    }, 17000);
  
  setTimeout(
    function() {
      if (!skipped) {
        document.querySelector('#pills').style.opacity='1';
      }
    }, 15000);

  //START SKIP FUNCTIONALITY
  const skip = () => {
    first.cancel();
    second.cancel();
    document.querySelector('#pills').style.opacity='1';
    document.querySelector('#destination').style.display='none';
    document.querySelector('#destination-1').style.display='none';
    document.querySelector('#source-show').style.display='block';
    document.querySelector('#source-show-1').style.display='block';
    document.querySelector('#skip').style.display='none';
    document.getElementById("language").removeAttribute('disabled');
  };
  document.getElementById("skip").addEventListener('click', skip);
  document.getElementById("skip").style.display = 'block';

  setTimeout(
    function() {
      document.getElementById("skip").style.display = 'none';
      document.getElementById("language").removeAttribute('disabled');
    }, 51000);
};

document.getElementById("start").addEventListener('click', startJourney);