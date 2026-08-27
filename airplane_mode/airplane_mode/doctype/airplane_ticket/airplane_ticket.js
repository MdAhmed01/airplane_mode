// Copyright (c) 2026, Ahmed Ansari and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Ticket", {
    validate(frm) {
        let items = [];

        frm.doc.add_ons.forEach(row => {
            if (items.includes(row.item)) {
                frappe.throw(
                    __("Add-on {0} has already been added.", [row.item])
                );
            }

            items.push(row.item);
        });
    }
});

