let ID = () => {
    return Date.now();
};

let calcularIdade = (dataPlantio) => {
    const plantio = new Date(dataPlantio);
    const hoje = new Date();

    let anos = hoje.getFullYear() - plantio.getFullYear();
    let meses = hoje.getMonth() - plantio.getMonth();

    if (meses < 0) {
        anos--;
        meses += 12;
    }

    return anos * 12 + meses;
};

let getPlantas = () => {
    const data = localStorage.getItem('plantas');
    return data ? JSON.parse(data) : [];
};

let salvarPlantas = (planta) => {
    localStorage.setItem('plantas', JSON.stringify(planta));
;}

let prepararCards = () => {
    const lista = document.getElementById('plantaLista');
    lista.innerHTML = '';

    const plantas = getPlantas();

    if (plantas.length === 0) {
        lista.innerHTML = `<p class="text-center">Nenhuma planta cadastrada.</p>`;
        return;
    }

    plantas.forEach(item => {
        const idade = calcularIdade(item.plantio);

        const card = document.createElement('div');
        card.className = 'col-md-4';

        card.innerHTML = `
        <div class="card h-100 shadow-sm">
            <div class="card-body">
            <h5 class="card-title">${item.nomePopular}</h5>
            <h6 class="card-subtitle mb-2 text-muted"><em>${item.nomeCientifico}</em></h6>
            <p class="card-text"><strong>Produção média:</strong> ${item.producaoMedia} Kg</p>
            <p class="card-text"><strong>Data do plantio:</strong> ${new Date(item.plantio).toLocaleDateString('pt-BR')}</p>
            <p class="card-text"><strong>Idade:</strong> ${idade} mês(es)</p>
            </div>
        </div>
        `;

        lista.appendChild(card);
    });
}

// FORMS

document.getElementById('formCadastro').addEventListener('submit', function (e) {
    e.preventDefault();

    if (!this.checkValidity()) {
        e.stopPropagation();
        this.classList.add('was-validated');
        return;
    }

    const novaPlanta = {
        id: ID(),
        nomePopular: document.getElementById('nomePopular').value.trim(),
        nomeCientifico: document.getElementById('nomeCientifico').value.trim(),
        producaoMedia: parseFloat(document.getElementById('producaoMedia').value),
        plantio: document.getElementById('dataPlantio').value,
    };

    const plantas = getPlantas();
    plantas.push(novaPlanta);
    salvarPlantas(plantas);

    this.reset();
    this.classList.remove('was-validated');

    const modalEl = document.getElementById('modalCadastro');
    const modal = bootstrap.Modal.getInstance(modalEl);
    modal.hide();

    prepararCards();

});

document.addEventListener('DOMContentLoaded', prepararCards);