# -*- encoding: utf-8 -*-
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#
#    Copyright (c) 2013 Vauxoo - http://www.vauxoo.com/
#    All Rights Reserved.
#    info Vauxoo (info@vauxoo.com)
############################################################################
#    Coded by: moylop260 (moylop260@vauxoo.com)
#              Julio Serna (julio@vauxoo.com)
#              Isaac Lopez (isaac@vauxoo.com)
############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name" : "City_Romania",
    "version" : "1.0",
    "author" : "Vauxoo modifiyd by alexteodor",
    "category" : "Localization/Romania",
    "description" : """This module creates the city model similar to states model and adds the field city_id on res partner.
it's for romania; cityes are took from https://github.com/romania/localitati
    """,
    "website" : "http://www.vauxoo.com/",
    "license" : "AGPL-3",
    "depends" : [
            "base",
        ],
    "demo" : [],
    "data" : [
        'res_city_view.xml',
        'partner_address_view.xml',
        'security/city_security.xml',
        'security/ir.model.access.csv',
#daca le aveam importate la o versiune anerioara si acum le comentez, 
#le va sterge cand fac update la modul

#orase fara diacritice
	'data/res.country.state.city.csv',
#daca nu ai importate judetele, trebuie sa le importi
#daca vrei sa nu ai diacritice trebuie sa schimbi numele fisierului 
#res.country.state_fara_diacritice in res.county.state.csv
#	'data/res.country.state.csv',
#importat banci
	'data/res.bank.csv',

    ],
    "installable" : True,
    "active" : False,
}
