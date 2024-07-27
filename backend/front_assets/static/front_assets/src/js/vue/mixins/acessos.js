const { isFundacao } = GLOBAL;
export default {
	data() {
		return {
			isGestorSAI: null,
			isGestorSAP: null,
			acessSAP: null,
			acessSAI: null,
			isFundacao: isFundacao(),
		};
	},
	mounted() {
		setTimeout(() => {
			this.isGestorSAI = document.getElementById("isGestorSAI").value == "True";
			this.isGestorSAP = document.getElementById("isGestorSAP").value == "True";
			this.acessSAI = document.getElementById("acessSAI").value == "True";
			this.acessSAP = document.getElementById("acessSAP").value == "True";
		}, 100);
	},
};
