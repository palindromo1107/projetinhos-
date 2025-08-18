let preparacoesCard = [{
        src: 'https://images.unsplash.com/photo-1541167760496-1628856ab772?q=80&w=1337&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
        titulo: 'Café Expresso',
        descricao: 'Café expresso ristreto com grãos selecionados.',
        preco: 'R$ 10',
    },
    {
        src: 'https://images.unsplash.com/photo-1512372388054-a322888e67a6?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
        titulo: 'Café em grãos',
        descricao: 'Café em grãos de terras vulcânicas.',
        preco: 'R$ 40',
    },
    {
        src: 'https://images.unsplash.com/photo-1599861425846-d4f19b180e77?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTl8fGNyb2lzc2FudCUyMGZvb2R8ZW58MHx8MHx8fDA%3D',
        titulo: 'Croissant',
        descricao: 'Farinha 0-0.',
        preco: 'R$ 30',
    },
];

let preparacoesCardapio = [];

let inserirPreparacao = () => {};

let getCartao = (item) => {
    return `<div class="col p-1">
            <div class="card">
            <img src="${item.src}" class="card-img-top" alt="...">
            <div class="card-body">
                <h5 class="card-title">${item.titulo}</h5>
                <p class="card-text">${item.descricao}</p>
                <a href="#" class="btn btn-primary">${item.preco}</a>
            </div>
            </div>
        </div>`;
};

let setCartaoCol = (cartao) => {
    let cartoesDiv = document.getElementById('cartoes');
    cartoesDiv.insertAdjacentHTML('beforeend', cartao);
};

let createCartoes = () => {
    // Mini teste no retorno das férias. Eba!\o/
    for (let item of preparacoesCard) {
        // Html completo referente a cada card com o conteúdo.
        let cartao = getCartao(item);

        // Inserir cartão dentro do código html na div com id cartoes.
        setCartaoCol(cartao);
    }
};

createCartoes();