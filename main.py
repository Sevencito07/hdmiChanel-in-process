<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi Página Simple</title>
    <style>
        body {

            font-family: Arial, sans-serif;
            text-align: center;
            margin: 0;
            background-color: #191b19;
            place-content:center;
        }
        .main-container{

           width:100%;
           height:100vh;
        }
       .container{
          margin-top:1rem;
          height:6rem;
          display:flex;
          flex-direction:row;
       }
       .box{
          margin-left:2rem;
          background-color: #193c7a;
          width: 5rem;
          height: 100%;
          border-radius:10px;
          border:2px solid #282d29;
       }
       .box.active{background-color:#cad9fa}
       span{
          font-family:Comic Sans MS, cursive;
          color:#d5dbd6;
          font-size:4.5rem
       }
      h2{color:#d5dbd6;}
      .container-set{
          height:14rem;
          margin-top:1.5rem;
          display:flex;
          flex-direction:row;
          place-content:ceneter;
}
     .box-on{
          background-color:#abb9bb ;
          width: 5rem;
          height: 5rem;
          border-radius:50%;
          border:2px solid #282d29;
          margin-top:1.7rem;

}
    .box-on:active{background-color:#001eec}
    .set-box{
          margin-left:2rem;
          background-color: #193c7a;
          width: 5rem;
          height: 100%;
          border-radius:10px;
          border:2px solid #282d29;
          display:flex;
          flex-direction:column;
          place-content:center;
          place-items:center;
}
    img{width:40px}
    .end-container{
          margin-left:2rem;
          diplay:flex;
          width:5rem;
          flex-direction:column;
          height:100%;

      }
    .box-zero{

          background-color: #193c7a;
          width: 5rem;
          height: 6rem;
          border-radius:10px;
          border:2px solid #282d29;
     }
    .box-zero.active{background-color:#cad9fa}
    .reset-button{margin-top:3.5rem}
    </style>
 <script>

         function saveValue(value){
              if(!localStorage.getItem("CH1")){
               localStorage.setItem("CH1",value)
             }
              else{
               localStorage.setItem("CH2",value)
              }};


     async function handleClick2() {
         alert('xxx')
        const numberCh = localStorage.getItem("CH1") + localStorage.getItem("CH2");
         try {
        const response = await fetch('http://192.168.4.49:5000/ch', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: numberCh
        });
        const data = await response.text();
        console.log("Respuesta del servidor:", data);
    } catch (error) {
        console.error("Error:", error);
    }

       setTimeout(() => {  
           localStorage.setItem("CH1","");
           localStorage.setItem("CH2","");
      }, 3000);

      }

    function resetClick(){
           localStorage.setItem("CH1","");
           localStorage.setItem("CH2","");
    }
</script>



</head>
<body>
 <div class="main-container">
 <div class="container">
  <button  class="box"  onclick="saveValue(1)"  ><span>1</span></button>
  <button  class="box" onclick="saveValue(2)"  ><span>2</span></button>
  <button  class="box" onclick="saveValue(3)"  ><span>3</span></button>
 </div>
  <div class="container">
  <button  class="box"onclick="saveValue(4)" ><span>4</span></button>
  <button  class="box" onclick="saveValue(5)" ><span>5</span></button>
  <button  class="box"onclick="saveValue(6)" ><span>6</span></button>
 </div>
 <div class="container">
  <button  class="box"onclick="saveValue(7)"  ><span>7</span></button>
  <button  class="box"onclick="saveValue(8)"  ><span>8</span></button>
  <button  class="box"onclick="saveValue(9)"  ><span>9</span></button>
 </div>
 <div class="container-set">
  <button onclick="test()" class="set-box" >
  <span>+</span>
  <img src="loud-speaker.png"/>
  <span>-</span>

 </button>
  <div class="end-container">
  <button id="active" class="box-zero"onclick="saveValue(0)"  ><span>0</span></button>
  <button onclick="handleClick2()"  class="box-on" ></button>
  </div>
  <button  class="set-box" >
  <span>+</span>
  <h2>CH</h2>
  <span>-</span>
  </button>
 </div>

 <button onclick="resetClick()" class="reset-button">reset</button>
 </div>
<script>
 const botones = document.querySelectorAll('.box');

    // Añadir un evento de clic a cada botón
    botones.forEach(boton => {
      boton.addEventListener('click', () => {
        // Alternar la clase 'active' en el botón clickeado
        boton.classList.toggle('active');
      setTimeout(() => {
            boton.classList.remove('active');
      }, 1000)
      });
    });

 const buttonZero = document.getElementById('active');

    buttonZero.addEventListener('click', () => {
      // Alterna la clase 'active' al botón
      buttonZero.classList.toggle('active');
      setTimeout(() => {
            buttonZero.classList.remove('active');
      }, 1000);
    });
</script>
</body>
</html>
