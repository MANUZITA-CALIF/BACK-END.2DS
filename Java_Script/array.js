const frutas = ['Maça', 'Banana', 'Laranja'];
console.log(frutas.length);
console.log(frutas);
frutas.push('Manga');
console.log(frutas);
frutas.pop();
console.log(frutas);

const citricas = frutas.slice(0,2);
console.log(citricas);

frutas.slice(1,0, 'Kiwi');
console.log(frutas);

const verduras = ['Cenoura', 'Batata'];
//const frutaseverduras = frutas.concat(verduras);
console.log(frutas.concat(verduras));