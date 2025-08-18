const addItemCardapioTable = (itemCardapio) => {
    let itensCardapioTBody = document.getElementById('itensCardapioTBody');
    let itemCardapioTr = `<tr>
    <th scope="row">1</th>
    <td>${itemCardapio.nome}</td>
    <td>${itemCardapio.preco}</td>
    <td>${itemCardapio.descricao}</td>
    </tr>`;

    itensCardapioTBody.insertAdjacentHTML('beforeend', itemCardapioTr);
};

const carregarTabela = () => {
    let itensCardapio = JSON.parse(localStorage.getItem('itensCardapio'));

    for (let itemCardapio of itensCardapio) {
        addItemCardapioTable(itemCardapio);
    }
};

const setPreparacaoFormValues = (nome = '', descricao = '', preco = '') => {
    const nomeInput = document.querySelector('#nome');
    const descricaoInput = document.querySelector('#descricao');
    const precoInput = document.querySelector('#preco');

    nomeInput.value = nome;
    descricaoInput.value = descricao;
    precoInput.value = preco;
};

const handleSubmit = (event) => {
    event.preventDefault();
    // let nomeInput = document.getElementById('nome');
    // let nome = nomeInput.value;
    // let precoInput = document.getElementById('preco');
    // let preco = precoInput.value;
    // let descricaoInput = document.getElementById('descricao');
    // let descricao = descricaoInput.value;
    // let itemCardapio = new Cardapio();
    // let itemCardapio = { nome, preco, descricao };

    // Dados do formulário -> criação do objeto.
    let cardapioForm = document.getElementById('itemCadastrarForm');
    // cardapioForm = event.target;
    let cardapioFormData = new FormData(cardapioForm);
    let itemCardapio = Object.fromEntries(cardapioFormData);

    // Adicionam o valor no localstorage.
    itensCardapio.push(itemCardapio);
    localStorage.setItem('itensCardapio', JSON.stringify(itensCardapio));

    // Adicionar na tabela.
    addItemCardapioTable(itemCardapio);

    // Limpar os valores do formulário.
    cardapioForm.reset();
    setPreparacaoFormValues();

    // Fechar o modal.
    $('#cardapioModal').modal('toggle');

    Toastify({
        text: 'Item do cardápio adicionado com sucesso!',
        duration: 3000, // Duration in milliseconds (3 seconds)
    }).showToast();
};

let itemCadastrarForm = document.getElementById('itemCadastrarForm');
itemCadastrarForm.onsubmit = handleSubmit;
// itemCadastrarForm.addEventListener('submit', handleSubmit);

let body = document.body;
body.onload = carregarTabela;
