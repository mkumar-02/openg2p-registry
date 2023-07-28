# Part of OpenG2P Registry. See LICENSE file for full copyright and licensing details.
{
    "name": "G2P Registry: Rest API",
    "category": "G2P",
    "version": "15.0.1.1.0",
    "sequence": 1,
    "author": "OpenG2P",
    "website": "https://openg2p.org",
    "license": "Other OSI approved licence",
    "development_status": "Production/Stable",
    "depends": [
        "base",
        "mail",
        "contacts",
        "component",
        "base_rest",
        "pydantic",
        "base_rest_pydantic",
        "extendable",
        "g2p_registry_group",
        "g2p_registry_individual",
        "base_rest_auth_user_service",
    ],
    "external_dependencies": {"python": ["extendable-pydantic", "pydantic==1.10.10"]},
    "data": [
        "security/g2p_security.xml",
        "security/ir.model.access.csv",
    ],
    "assets": {},
    "demo": [],
    "images": [],
    "application": True,
    "installable": True,
    "auto_install": False,
}
