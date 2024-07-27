export default {
	data() {
		return {
			isOpen: false,
			haveNotification: false,
		};
	},
	// updated() {
	// 	console.log(this.haveNotification, "haveNotification");

	// },

	methods: {
		openNotifications() {
			this.isOpen = true;
		},
		closeNotifications() {
			this.isOpen = false;
		},
		updatedNotification(param) {
			// console.log("ai meu deus", param)
			this.haveNotification = param;
		},
	},
};
