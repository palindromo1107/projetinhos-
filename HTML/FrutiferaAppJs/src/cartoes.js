let preparacoesCardapio = [];

let inserirPreparacao = () => {};

let getCartao = (item) => {
    return `
    <div class="card h-100 shadow-sm">
    <div class="card-body">
    <h5 class="card-title">${item.nomePopular}</h5>
    <h6 class="card-subtitle mb-2 text-muted"><em>${item.nomeCientifico}</em></h6>
    <p class="card-text"><strong>Produção média:</strong> ${item.producaoMedia} Kg</p>
    <p class="card-text"><strong>Data do plantio:</strong> ${new Date(item.dataPlantio).toLocaleDateString('pt-BR')}</p>
    <p class="card-text"><strong>Idade:</strong> ${idadeMeses} mês(es)</p>
    </div>
    </div>`;
};

let setCartaoCol = (cartao) => {
    let cartoesDiv = document.getElementById('cartoes');
    cartoesDiv.insertAdjacentHTML('beforeend', cartao);
};

let createCartoes = () => {
    for (let item of preparacoesCard) {
        let cartao = getCartao(item);
        setCartaoCol(cartao);
    }
};

createCartoes();