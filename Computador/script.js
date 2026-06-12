// variavel inicial do contador

let count = 0;

// Selecionando o visor do valor e todos os botões
const value = document.querySelector("value");
const btns = document.querySelectorAll(".btn")

//Percorrendo cada botão da lista 

btns.forEach(function(btn) { 
    btn.addEventListener("click", funcion (e) {
        //Pega as classes de botão que foi criado 
        const style = e.correntTarget.classList;
        
        //Virifica qual botão qual foi clicado e 
        // altera o valor
        if (styles.contains("decrease")){
            count --;
         } else if (style.cointains("increase")){
            count ++;
        } else {
        count = 0
        }

        // logica para mudar a cor do texto dependendo
        // do valor
        if (count > 0) {
            value.style.color = "green";
        }
        if (count <0)
            value.style.color = "red";

        if (count === 0) {
            value.style.color = "#222"; //Preto/Cinza 
            // Escuro

        }

        // Atuaiza o Texto na Tela

        value.textContent = count;
    });