let itens = [
{
    src: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRSz_yqHRav9n018Zx0lQAyVOnC-q2tHFc9Ug&s',
    titulo: 'Cafe',
    descricao: 'Descrição: Ta muito caro',
    preco: '1 rim',
},
{
    src: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTZ30SD-SUbdOx8KptO74oRBnVOc7_sS-BNfA&s',
    titulo: 'picanha',
    descricao: 'Desceição: Faz o L',
    preco: '100 Milhões',
},
{
    src: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTsU6ZqOwmGm2P5xVTdOaCa9KjgkSB8hEVRtw&s',
    titulo: 'luz azul',
    descricao: 'Descrição: Fica azul',
    preco: '10 R$',
}
]
let getCartao = (item) =>{
 return `<div class="col p-1">
        <div class="card">
            <img src="${item.src}" alt="...">
            <div class="card-body">
                <h5 class="card-title">${item.titulo}</h5>
                <p class="card-text">${item.descricao}</p>
                <a href="#" class="btn btn-primary">${item.preco}</a>
            </div>
        </div>
    </div>`;
};
let setCartaoCol = (cartao) =>{
    let cartoesDiv = document.getElementById('cartoes');
    cartoesDiv.insertAdjacentHTML('beforeend', cartao);
};
let createCartoes = () =>{
    for (let item of itens) {
 // html completo referente a cada card com o conteudo
        let cartao = getCartao(item);
 // Inserir cartao dentro do código html na div com id cartoes.
        setCartaoCol(cartao);
    }
};
createCartoes();