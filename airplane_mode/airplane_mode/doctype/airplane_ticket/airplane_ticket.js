// Copyright (c) 2026, Ahmed Ansari and contributors
// For license information, please see license.txt

frappe.ui.form.on('Airplane Ticket', {
	refresh(frm) {
		// your code here
	},
    flight_price(frm){
        frm.trigger("update_total_amount")

    },
    update_total_amount(frm){
        let items_amount=0;
        for(let item of frm.doc.add_ons) {
            items_amount += item.amount;
    }
    const amounts = items_amount + frm.doc.flight_price;
        frm.set_value("total_amount",amounts);

    }    
});




frappe.ui.form.on('Airplane Ticket Add-on Item', {
	refresh(frm) {
		// your code here
	},
    amount(frm,cdt,cdn) {
        frm.trigger("update_total_amount");

    },
    add_ons_remove(frm){
        frm.trigger("update_total_amount")
    }
})

