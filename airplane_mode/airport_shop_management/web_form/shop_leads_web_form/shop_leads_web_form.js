frappe.ready(function() {
	
	if(window.location.pathname.endsWith("/new")){
		frappe.web_form.set_value("shop","{{Shop}}")
	}
})