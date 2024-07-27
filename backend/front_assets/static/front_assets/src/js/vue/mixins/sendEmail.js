const { api, getChoicesActive, showToastify } = GLOBAL;

export default {
	data() {
		return {
			state: {
				sending: false,
			},
		};
	},

	computed: {
		btnClass() {
			return { disabled: this.state.sending };
		},
	},

	methods: {
		clearFields(els, type) {
			if (type === "select") {
				console.log("passou");

				els.forEach((s) => {
					const select = getChoicesActive(s.id, listOfChoices);
					select?.setChoiceByValue(0);
				});
			} else if (type === "input") {
				console.log(els, "input");
				els.forEach((i) => (i.value = ""));
			}
		},

		/**
		 * @summary Callback que recebe um  field de formulario e adiciona
		 * @summary remove classe se for valido
		 * @param {HTMLFormElement} field
		 * @return {Boolean} - diz se esta valido ou nao
		 */
		toogleValideField(field) {
			const label = field.closest("[js-field]")?.querySelector("label");
			const valid = field.checkValidity();

			if (valid && label) {
				label.classList.remove("error");
			} else {
				label.classList.add("error");
			}

			return valid;
		},

		data() {
			return {
				modelo: document.querySelector("#select-modelo")?.value,
				responsaveis: getChoicesActive("select-responsaveis", listOfChoices),
				cliente: document.querySelector("#select-cliente")?.value,
				titulo: document.querySelector("#input-titulo")?.value,
				corpo_email: document.querySelector("#textarea-corpo-email")?.value,
			};
		},

		elementos() {
			return {
				modeloEl: document.querySelector("#select-modelo"),
				responsaveisEl: getChoicesActive("select-responsaveis", listOfChoices),
				clienteEl: document.querySelector("#select-cliente"),
				tituloEl: document.querySelector("#input-titulo"),
				corpo_emailEl: document.querySelector("#textarea-corpo-email"),
			};
		},

		/**
		 * @summary  envia o request de e-mail se for valido
		 * fecha o modal quando enviado e limpa os campos
		 * @param {Event} Callback evento
		 */
		async sendEmail({ currentTarget }) {
			NProgress.start();

			const form = currentTarget.closest("form");

			const fields = [...form.querySelectorAll("[name]")];

			fields?.map(this.toogleValideField);

			const valid = fields?.every((f) => f.checkValidity());

			if (!valid) {
				showToastify("⚠️ Preencha todos os campos obrigatorios.");
				return;
			}
			const { modelo, responsaveis, cliente, titulo, corpo_email } =
				this.data();
			const { modeloEl, responsaveisEl, clienteEl, tituloEl, corpo_emailEl } =
				this.elementos();

			const data = {
				modelo,
				contatos: responsaveis?.getValue()?.map((i) => i.value),
				cliente: Number(cliente),
				titulo,
				corpo_email,
			};

			try {
				this.state.sending = true;
				const request = await axios.post(window.home_data.url_email, data);
				showToastify("✅ Email enviado com sucesso.");

				this.clearFields([modeloEl, responsaveisEl, clienteEl], "select");
				this.clearFields([tituloEl, corpo_emailEl], "input");
				modal_padrao_vue.closeModal();
			} catch (e) {
				console.log(e);
				showToastify("❌ Ocorreu um erro ao enviar o email.");
			} finally {
				this.state.sending = false;
				NProgress.done();
			}
		},

		closeSendEmail() {
			const { modeloEl, responsaveisEl, clienteEl, tituloEl, corpo_emailEl } =
				this.elementos();
			this.clearFields([modeloEl, responsaveisEl, clienteEl], "select");
			this.clearFields([tituloEl, corpo_emailEl], "input");
			modal_padrao_vue.closeModal();
		},

		async getContatos(idCliente) {
			const { data } = this.isFundacao
				? await api.get(`/api/contatos/?fundacao=${idCliente}`)
				: await api.get(`/api/contatos/?cliente_pf=${idCliente}`);
			return data;
		},

		async handleChangeCliente(choicesClientes, choicesResponsaveis) {
			choicesResponsaveis?.clearStore();
			const idCliente = choicesClientes.getValue()?.value;
			const data = await this.getContatos(idCliente);
			const optionsContatos = data.map(({ id, nome, principal }) => ({
				value: id,
				label: nome,
				selected: principal,
			}));

			choicesResponsaveis?.setChoices(
				[...optionsContatos],
				"value",
				"label",
				true
			);
		},

		async openSendEmail(idPass) {
			_BIG("id_cliente");
			console.log(idPass);
			NProgress.start();

			const choicesClientes = getChoicesActive(
				"select-cliente",
				window.listOfChoices
			);
			const choicesResponsaveis = getChoicesActive(
				"select-responsaveis",
				window.listOfChoices
			);

			choicesResponsaveis?.clearStore();
			choicesClientes?.clearStore();

			const optionsClientes = todosClientesUsuario.map(({ id, nome }) => ({
				value: id,
				label: nome,
				selected: id == idPass,
			}));

			const data = await this.getContatos(idPass);
			const optionsContatos = data.map(({ id, nome, principal }) => ({
				value: id,
				label: nome,
				selected: principal,
			}));

			choicesResponsaveis?.setChoices(
				[...optionsContatos],
				"value",
				"label",
				true
			);
			choicesClientes?.setChoices([...optionsClientes], "value", "label", true);

			choicesClientes.passedElement.element?.addEventListener("change", () =>
				this.handleChangeCliente(choicesClientes, choicesResponsaveis)
			);
			modal_padrao_vue.openModal("enviar_email");

			NProgress.done();
		},
	},
};
