"""Oct 29, 2026 answers for five open questions. Applied on top of the approved checklist.

Original steps stay in earlierSteps. Confirmed facts replace 'to be confirmed'.
Points the research note still leaves open stay flagged.
"""

FLORIDA_ALERT = (
    "Keep your Florida licences valid. Do not switch them to Indiana licences before the move. "
    "A Florida licence can be exchanged in Saint-Martin for cars (category B) and motorcycles (category A). "
    "An Indiana licence cannot be exchanged. You would have to pass the French driving test. "
    "Source: Interior Ministry reciprocity list of May 1, 2026, and the French consulate in Chicago. This is not legal advice."
)

CHECKED = "Opened OK on Oct 29, 2026."
BLOCKED = (
    "The site blocked an automatic check on Oct 29, 2026 (not a dead page). "
    "This is still the official address. Open it in Chrome. A research pass the same day read the page."
)


def L(label, url, state, detail):
    return {"label": label, "url": url, "state": state, "detail": detail}


UPDATES = {
    "ld12": {
        "steps": [
            "A stay over 90 days needs a French long-stay visa issued before you leave, and it must cover Saint-Martin.",
            "Saint-Martin is outside the Schengen area. A Schengen visa alone does not cover it.",
            "For 90 days in any 180, a US passport does not need a visa. That visit does not let you settle or switch to residence on the island. You would go back to the United States to apply.",
            "You do not have to file the visa before November 19, 2026. You can apply from Indiana. Chicago is the nearest visa centre to New Albany. Washington, DC decides every US application.",
            "Write down the departure date you will actually use. You cannot file more than 3 months before that date.",
            "This is planning help, not immigration advice.",
        ],
        "docs": [
            "A departure date you both agree, even if it is later than the lease end.",
            "Nothing has to be filed before November 19. Before that date, order the Florida papers you will need later: apostilled birth and marriage records, bank statements, and the insurance certificate.",
        ],
        "tips": [
            "France-Visas says long-stay files cannot be sent more than 3 months before departure, to book the centre at least 1 month ahead, and to allow at least 15 days for processing. There is no fast track.",
            "You may use any of the 11 TLScontact centres, not only the one for your state. Florida's district is Miami (2125 Biscayne Blvd, suite 400A). Indiana's district is Chicago (405 W Superior St, suite 100B).",
        ],
        "verify": "Current visa-centre fees, and how long they keep your passport. Also whether an Indiana address, such as a son's home, is accepted as proof that you live in the United States. Ask TLScontact or the consulate.",
        "links": [
            L("France-Visas: long-stay visa", "https://www.france-visas.gouv.fr/en/visa-de-long-sejour", "flagged", BLOCKED),
            L("France-Visas: applying from the United States", "https://france-visas.gouv.fr/en/etats-unis-d-amerique", "flagged", BLOCKED),
            L("French version of the United States page", "https://france-visas.gouv.fr/united-states-of-america", "flagged", BLOCKED),
            L("Which French office covers your state", "https://us.diplomatie.gouv.fr/fr/presence-francaise/demarches-administratives-qui-madresser", "verified", CHECKED + " Page updated January 27, 2026. Florida is Miami. Indiana is Chicago."),
            L("service-public.fr: visas for overseas territories", "https://www.service-public.gouv.fr/particuliers/vosdroits/F10610", "verified", CHECKED),
        ],
    },
    "ld27": {
        "tips": [
            "One office, the Consulate General in Washington, DC, decides every US application. You can book any of the 11 centres.",
        ],
        "links": [
            L("France-Visas: applying from the United States", "https://france-visas.gouv.fr/en/etats-unis-d-amerique", "flagged", BLOCKED),
        ],
    },
    "ld28": {
        "steps": [
            "Open the TLScontact page for visa centres in the United States.",
            "You can book any of the 11 centres. From Indiana, Chicago is the closest: 405 W Superior St, suite 100B. If you are still in Florida, Miami is 2125 Biscayne Blvd, suite 400A.",
            "Book at least 1 month before you plan to go to the appointment. Allow at least 15 days after that for a decision. There is no fast track.",
            "Do not book more than 3 months before your departure date. For a March 1, 2027 departure, that means filing no earlier than about December 1, 2026.",
            "You do not have to do this before November 19, 2026. Pick the departure date first.",
        ],
        "docs": [
            "The departure date, so you can count back 3 months and 1 month.",
            "The centre you will use. Chicago if you apply from Indiana.",
            "The service fee shown on the TLScontact page that day. The amount was not copied here.",
        ],
        "tips": [
            "Washington, DC decides the application even if you go to Chicago or Miami.",
            "The old note that a November 19 departure might already be too late to file is replaced by this: nothing has to be filed before November 19. A visa for a departure only three weeks away would not meet the one-month booking advice. Choose a later departure if you need the visa before you fly.",
        ],
        "verify": "The current TLScontact service fee, the visa fee, and how long they keep the passport. Also whether an Indiana address is accepted as your US residence. Ask TLS or the consulate.",
        "links": [
            L("TLScontact: France visa centres in the US", "https://visas-fr.tlscontact.com/en-us/country/us", "flagged", BLOCKED),
            L("France-Visas: applying from the United States", "https://france-visas.gouv.fr/en/etats-unis-d-amerique", "flagged", BLOCKED),
            L("Which French office covers your state", "https://us.diplomatie.gouv.fr/fr/presence-francaise/demarches-administratives-qui-madresser", "verified", CHECKED + " Florida is Miami. Indiana is Chicago."),
        ],
    },
    "im01": {
        "steps": [
            "Open the France-Visas visa wizard.",
            "Set the destination to Saint-Martin, not mainland France and not the Dutch side.",
            "Set the purpose to a private stay or visitor, unless the wizard uses different words.",
            "The wizard is what shows the exact visa name and the document list. That exact label is still to be confirmed until you run it.",
        ],
        "tips": [
            "Saint-Martin is outside Schengen. The territory printed on the sticker matters. 'DFA' covers Saint-Martin and Saint-Barthélemy. 'France sauf CTOM' does too. Those phrases were read from the official texts on Oct 29. Open the pages in Chrome.",
        ],
        "verify": "The exact visa name for a retiree going to Saint-Martin: a VLS-TS 'visiteur', or a visa that says you must ask for a residence card within 2 months. Run the wizard with destination Saint-Martin.",
        "links": [
            L("France-Visas visa wizard", "https://www.france-visas.gouv.fr/en/web/france-visas/visa-wizard", "flagged", BLOCKED),
            L("France-Visas: France is not all in Schengen", "https://france-visas.gouv.fr/web/france-visas/la-france-dans-l-espace-schengen", "flagged", BLOCKED),
            L("Interior Ministry: visas for overseas territories", "https://www.immigration.interieur.gouv.fr/limmigration-en-france/visas-en-france/visas-pour-loutre-mer", "flagged", BLOCKED),
        ],
    },
    "ld29": {
        "steps": [
            "When the sticker is in the passport, read the type, the dates, and the places it covers.",
            "It should name Saint-Martin, or say DFA, or say France sauf CTOM. Those wordings cover Saint-Martin.",
            "There are two long-stay kinds. A VLS-TS is validated online on ANEF within 3 months of arrival. A sticker that says you must ask for a residence card within 2 months means you go to the préfecture.",
            "The exact kind a retiree receives for Saint-Martin is still to be confirmed. The wizard is the place that shows it before you apply.",
        ],
        "docs": [
            "The passport with the sticker.",
            "A photo of the sticker, stored with your other scans. Do not type the visa number in the notes box.",
        ],
        "verify": "Which of the two stickers the consulate issues for a Saint-Martin visitor. Check the sticker you receive, and run the wizard before you apply.",
        "links": [
            L("France-Visas: long-stay visa", "https://www.france-visas.gouv.fr/en/visa-de-long-sejour", "flagged", BLOCKED),
            L("Légifrance: Saint-Martin entry rules (2021 amendment)", "https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000043814282", "flagged", BLOCKED),
        ],
    },
    "ld31": {
        "steps": [
            "Read the sticker first. Do this online step only if it is a VLS-TS.",
            "If the sticker says to ask for a residence card within 2 months, skip ANEF validation and use the préfecture step instead.",
            "If it is a VLS-TS, open ANEF within 3 months of arrival and pay the tax the screen shows.",
            "If ANEF will not accept a Saint-Martin address, stop and ask the préfecture. Do not type a mainland address.",
        ],
        "docs": [
            "The visa sticker.",
            "A card for the tax. Pay the amount on the ANEF screen. An older figure of about €269 is not confirmed. To be confirmed.",
        ],
        "verify": "Whether ANEF validation works with a Saint-Martin address, or whether the préfecture does the first validation. Ask the préfecture. The tax amount is whatever ANEF shows. Confirm that number on the screen.",
        "links": [
            L("ANEF: online services for foreigners", "https://administration-etrangers-en-france.interieur.gouv.fr/particuliers/#/", "verified", CHECKED),
        ],
    },
    "ld35": {
        "steps": [
            "In Saint-Martin, the first residence-permit application is still on paper at the préfecture, rue de Spring, Concordia.",
            "Renewals moved online to ANEF on September 1, 2024. The préfecture said it would stop taking paper renewals after that date.",
            "Bring the document list from the visiteur card page, and ask the préfecture if their paper file wants anything different.",
            "A residence permit issued in Saint-Martin is valid in mainland France and the overseas departments, and the reverse is also true. That is in the immigration code. Open the page in Chrome. This is not immigration advice.",
        ],
        "docs": [
            "Passport, birth certificate, proof of address, proof of resources, photos, and the signed promise not to work.",
            "The fee. service-public.fr F302, checked Oct 29, 2026, says €350 for a first temporary visiteur card in the general rules (€300 tax plus €50 stamp). Whether Saint-Martin charges that amount is still to be confirmed.",
            "An appointment or the préfecture's paper instructions. Hours are in the contact card and are still to be confirmed, because the hours page would not reopen on Oct 29.",
        ],
        "verify": "The fee the Saint-Martin préfecture charges for a first visiteur card, and the exact paper document list it uses. The €350 figure is from the general service-public page, which does not name Saint-Martin.",
        "links": [
            L("Préfecture: first applications stay on paper; renewals moved online Sept 1, 2024", "https://www.saint-barth-saint-martin.gouv.fr/Actualites/SCI-Deploiement-d-une-demarche-en-ligne-a-saint-martin-a-partir-du-1er-septembre-2024", "verified", CHECKED),
            L("service-public.fr: visiteur card, including the €350 fee", "https://www.service-public.gouv.fr/particuliers/vosdroits/F302", "verified", CHECKED + " The page does not name Saint-Martin."),
            L("Immigration code: Saint-Martin permits (articles L443-1 to L443-3)", "https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006070158/LEGISCTA000042772094/", "flagged", BLOCKED),
        ],
    },
    "it01": {
        "steps": [
            "Open the SSA Payments Abroad Screening Tool.",
            "Saint-Martin is not named. Guadeloupe, Saint-Barthélemy, Sint Maarten (the Dutch side) and Martinique are sent to the Federal Benefits Unit in Santo Domingo, not Paris. French Saint-Martin is not on that list.",
            "The Santo Domingo unit serves the Caribbean islands and Colombia. That strongly suggests it is the office to ask. It is not written down as the office for French Saint-Martin.",
            "Email FBU.Santo.Domingo@ssa.gov, or call SSA at 1-800-772-1213, and ask which office serves French Saint-Martin and whether payments continue there.",
            "US citizens can generally keep Social Security while living abroad. The blocks are a few countries, such as Cuba and North Korea. France's overseas areas are not among them. Medicare generally does not pay for care outside the United States.",
        ],
        "docs": [
            "A my Social Security login if you have one. Do not type the claim number in the notes box.",
            "The question, written down: which office serves French Saint-Martin, and will payments continue there?",
        ],
        "tips": [
            "Do not mail the form to the Federal Benefits Unit in Paris. That was the older Scout note. It is kept below as earlier wording. Paris is the office for France. It is not named for Saint-Martin.",
            "SSA staff from Santo Domingo held a walk-in day on the French side, in Grand Case, in May 2023. Appointments were by email to FBU.Santo.Domingo@ssa.gov. That shows they have come to the French side. It still does not name them as your permanent office.",
        ],
        "verify": "That the Santo Domingo Federal Benefits Unit is the office for French Saint-Martin. Ask them by email at FBU.Santo.Domingo@ssa.gov or call SSA at 1-800-772-1213 before you move. The national number is the one given for this question. Confirm it on SSA's own contact page when you call.",
        "links": [
            L("SSA: Payments Abroad Screening Tool", "https://www.ssa.gov/international/payments_outsideUS.html", "flagged", BLOCKED),
            L("SSA: which office serves which country", "https://www.ssa.gov/foreign/foreign.htm", "flagged", BLOCKED),
            L("US Embassy Santo Domingo: Social Security", "https://do.usembassy.gov/social-security/", "verified", CHECKED + " The Santo Domingo unit serves the Caribbean islands and Colombia. French Saint-Martin is not named."),
            L("US Embassy Bridgetown: 2023 benefits visits in Grand Case", "https://bb.usembassy.gov/message-to-u-s-citizens-social-security-and-federal-benefits-consultations-in-anguilla-and-st-martin/", "verified", CHECKED),
            L("SSA leaflet: payments while outside the United States", "https://www.ssa.gov/pubs/EN-05-10137.pdf", "flagged", BLOCKED),
        ],
    },
    "mv_ssa": {
        "steps": [
            "Before you leave the Florida address, give SSA a forwarding address in Indiana.",
            "Tell SSA the Saint-Martin address only once you have actually moved.",
            "Ask which office to use. Email FBU.Santo.Domingo@ssa.gov or call 1-800-772-1213. Do not send papers to the Paris office unless SSA tells you to.",
        ],
        "docs": [
            "The Indiana mailing address you want SSA to use until you move.",
            "The Saint-Martin address, later, once you have it.",
        ],
        "tips": [
            "The older instruction to mail SSA-1199-FR to the US Embassy in Paris is kept in the earlier wording. Do not follow it unless SSA says Paris is your office.",
        ],
        "verify": "Which Federal Benefits Unit serves French Saint-Martin. Santo Domingo is the office for the neighboring islands and has visited Grand Case, but French Saint-Martin is not named on the list.",
        "links": [
            L("SSA: which office serves which country", "https://www.ssa.gov/foreign/foreign.htm", "flagged", BLOCKED),
            L("SSA: a beneficiary leaving the United States", "https://www.ssa.gov/foreign/leaving_us.htm", "flagged", BLOCKED),
            L("US Embassy Santo Domingo: Social Security", "https://do.usembassy.gov/social-security/", "verified", CHECKED),
        ],
    },
    "b16": {
        "steps": [
            "The simplest plan is to keep a US bank account and let Social Security pay that account.",
            "Before you leave Florida, ask your US bank if it will keep the account open once you have a foreign address. Get the answer in writing if you can.",
            "A euro deposit into a Saint-Martin bank is not confirmed. France, Martinique and Sint Maarten are on SSA's direct-deposit list. French Saint-Martin is not named.",
            "If you still want a euro deposit, ask SSA whether a Saint-Martin IBAN is accepted before you close the US account. The form is SSA-1199. The bank fills in its section. Do not mail it to Paris unless SSA says to.",
        ],
        "docs": [
            "A US account you will keep open.",
            "The bank's written answer about a foreign address.",
            "If you ask about a euro account: the IBAN, which the bank writes on the form. Do not paste the full IBAN into notes.",
        ],
        "tips": [
            "Give SSA the Indiana forwarding address before you leave Florida. Tell them the foreign address only after you move.",
        ],
        "verify": "Whether SSA will deposit into a euro account at a Saint-Martin bank. Keep the US account until SSA says yes.",
        "links": [
            L("SSA: international direct deposit country list", "https://www.ssa.gov/international/countrylist6.htm", "flagged", BLOCKED),
            L("SSA: direct deposit forms", "https://www.ssa.gov/forms/ssa-1199.html", "flagged", BLOCKED),
        ],
    },
    "hc01": {
        "steps": [
            "Open the service-public page on PUMa (F34308).",
            "People who do not work in France can get cover based on living there. The page says you wait 3 months before the rights open, then you must live there at least 6 months a year.",
            "A 2026 law creates a yearly charge for residents who do not work and do not pay French social charges. The decree that sets the amount was still pending when the page was checked.",
            "Ask the CGSS desk in Marigot whether those same rules, and that new charge, apply in Saint-Martin. Saint-Martin sets its own taxes, but this health desk is the CGSS of Guadeloupe.",
        ],
        "docs": [
            "Nothing to sign yet.",
            "A note of the 3-month wait and the 6-month rule, and that the new charge has no published amount yet.",
        ],
        "tips": [
            "For retirees from outside the European Union, service-public also points to CLEISS, the office for social security abroad. Phone +33 1 45 26 33 41. Phone hours on that page: Monday and Wednesday 9:00 a.m. to 12:30 p.m. Tuesday, Thursday and Friday 1:30 p.m. to 4:30 p.m.",
            "Non-EU residents must show a valid residence document, such as a long-stay visa that counts as a residence permit, a residence card, or a receipt. That list is on service-public F13842, which opened on Oct 29, 2026.",
        ],
        "verify": "Whether the mainland 3-month wait and the new 2026 charge apply in exactly the same way in Saint-Martin. Ask the CGSS desk. The amount of the new charge is not published yet.",
        "links": [
            L("service-public.fr: what PUMa is", "https://www.service-public.gouv.fr/particuliers/vosdroits/F34308", "verified", CHECKED + " The page's own check date shown there was May 13, 2026."),
            L("ameli.fr: PUMa and form S1106", "https://www.ameli.fr/assure/droits-demarches/principes/protection-universelle-maladie", "flagged", BLOCKED),
            L("service-public.fr: retirees and health cover abroad (CLEISS)", "https://www.service-public.gouv.fr/particuliers/vosdroits/F12859", "verified", CHECKED),
            L("service-public.fr: which residence papers count", "https://www.service-public.gouv.fr/particuliers/vosdroits/F13842", "verified", CHECKED),
        ],
    },
    "hc03": {
        "docs": [
            "Passport for each person.",
            "A valid residence document. What counts is on service-public F13842.",
            "Proof of address.",
            "Birth certificates, and the marriage certificate if you are married. Whether this desk wants them apostilled and translated is still to be confirmed. Order them now anyway. The visa file needs them too.",
            "The exact list the Marigot desk wants is still to be confirmed. Ask when you call 36 46, before you mail anything.",
        ],
        "verify": "The exact document list the CGSS desk in Saint-Martin wants, including whether the birth and marriage certificates must be apostilled and translated.",
        "links": [
            L("service-public.fr: which residence papers count", "https://www.service-public.gouv.fr/particuliers/vosdroits/F13842", "verified", CHECKED),
        ],
    },
    "hc04": {
        "steps": [
            "Call 36 46. From the United States dial +33 1 84 90 36 46.",
            "Say you want an appointment at the Accueil Maladie de Saint-Martin, Spring Concordia, 6 rue Jean-Luc Hamlet, 97150.",
            "You can also book from an ameli account once you have one. Until then, use the phone.",
            "Write the date and time in your notes.",
        ],
        "docs": [
            "The PUMa file, once the document list is confirmed.",
            "Do not count on walking in. The directory lists weekday mornings only.",
        ],
        "tips": [
            "Front-desk hours on the official directory, last changed March 28, 2024: Monday, Tuesday and Thursday 7:30 a.m. to noon. Wednesday and Friday 8:00 a.m. to noon. Those hours were checked again on Oct 29, 2026.",
            "A line on the same page for 7:30 a.m. to 11:00 a.m. is the phone relay for deaf and hard-of-hearing people, not the front desk.",
            "The Guadeloupe CGSS website's own office page was down on Oct 29, 2026 (it returned an error). A search snippet from it showed different hours. Do not use that snippet. Confirm the hours when you call.",
        ],
        "verify": "The hours, when you call. The directory is the confirmed source, and it was last changed in 2024. The CGSS website was down on Oct 29, 2026, so a second official page could not be compared.",
        "links": [
            L("Service-public directory: CGSS Saint-Martin", "https://lannuaire.service-public.gouv.fr/collectivites-d-outre-mer/saint-martin/635a7d03-af7b-4cca-8f8b-1c28d5c6d692", "verified", CHECKED + " Page last changed March 28, 2024."),
            L("Santé.fr: the same Saint-Martin desk", "https://www.sante.fr/caisse-generale-de-securite-sociale-cgss-de-guadeloupe-accueil-de-saint-martin", "verified", CHECKED),
        ],
    },
    "v2": {
        "alert": FLORIDA_ALERT,
        "steps": [
            "The one-year clock starts when you become a resident, not on a short visit.",
            "You need your residence permit before you can exchange the licence.",
            "Exchange is done at the Collectivité, Service des titres, 7 rue Victor Maurasse, Marigot. You do not use the mainland ANTS website.",
            "The foreign licence is recognized for up to one year after you become a resident. The Collectivité page, updated September 9, 2026, says this. One sentence on that page also says 'en métropole'. Ask the desk if the same one-year clock is what they use in Saint-Martin.",
        ],
        "docs": [
            "The date you become a resident, once you have it.",
            "Your Florida licence, kept valid. Do not replace it with an Indiana licence.",
        ],
        "verify": "Whether the one-year clock on the Collectivité page, which uses the word métropole, is applied the same way by the Saint-Martin desk. Ask when you call 0590 87 61 91.",
        "links": [
            L("Collectivité: exchange a foreign licence", "https://www.com-saint-martin.fr/thematiques/mobilite-et-transport/demarches-permis-de-conduire/demande-dechange-de-permis-de-conduire-etranger", "verified", CHECKED + " Page updated September 9, 2026."),
        ],
    },
    "vh01": {
        "alert": FLORIDA_ALERT,
        "steps": [
            "Open the Interior Ministry reciprocity list of May 1, 2026, or the service-public simulator.",
            "Florida is on the list, for categories A and B (motorcycle and car).",
            "Indiana is not on the list. The French consulate in Chicago says there is no reciprocity agreement with Indiana.",
            "The licence must be valid, it must be a physical card, and the categories must have been earned by a theory and road test. A phone-only licence is not exchanged. An expired licence is not exchanged.",
            "If a licence cannot be exchanged, you take the French test. You do not have to do the 20-hour minimum of lessons if you already hold a valid foreign licence.",
            "Write down which state issued each current licence. If both are Florida, you can exchange them.",
        ],
        "docs": [
            "Each current licence, and the state name on it.",
            "A plan to renew any Florida licence that expires soon, before you leave Florida. Ask Florida (FLHSMV) about keeping a Florida licence after you leave the state. No FLHSMV page was added here.",
        ],
        "tips": [
            "Order the driving-rights certificate later. It has to be under 3 months old when you file the exchange.",
        ],
        "verify": "Which state issued each licence you hold today. If one of them is not Florida, say so in your notes and ask the desk before you rely on an exchange. Also still to be confirmed: whether a Saint-Martin licence is accepted for driving in mainland France and the rest of the European Union.",
        "links": [
            L("Interior Ministry reciprocity list, May 1, 2026 (PDF)", "https://www.diplomatie.gouv.fr/files/files/liste-reciprocite-hors-ue-et-eee-au-1er-mai-2026.pdf", "verified", CHECKED + " Florida (Floride) is listed for categories A and B. Indiana is not on the list."),
            L("service-public.fr: foreign-licence exchange simulator", "https://www.service-public.gouv.fr/simulateur/calcul/PermisEtrangerPermisFrancais", "verified", CHECKED),
            L("French consulate in Chicago: no reciprocity with Indiana", "https://us.diplomatie.gouv.fr/fr/permis-de-conduire-accords-de-reciprocite-avec-les-etats-de-la-circonscription-de-chicago", "verified", CHECKED),
            L("Collectivité: exchange a foreign licence", "https://www.com-saint-martin.fr/thematiques/mobilite-et-transport/demarches-permis-de-conduire/demande-dechange-de-permis-de-conduire-etranger", "verified", CHECKED),
        ],
    },
    "uw03": {
        "alert": FLORIDA_ALERT,
        "steps": [
            "Look at the expiry date on each Florida licence.",
            "If one expires soon, renew it with Florida before you leave Florida.",
            "Do not turn in a Florida licence for an Indiana licence while you are staying in Indiana.",
            "Ask Florida how a licence works after you no longer live in Florida. That Florida rule is not covered here.",
        ],
        "docs": [
            "Both physical Florida licences.",
            "The renewal fee Florida charges. That amount is Florida's fee. It was not copied here.",
        ],
        "verify": "Florida's own rule for keeping a licence after you move out of the state. Ask FLHSMV. No web address was added for that question.",
        "links": [
            L("Interior Ministry reciprocity list, May 1, 2026 (PDF)", "https://www.diplomatie.gouv.fr/files/files/liste-reciprocite-hors-ue-et-eee-au-1er-mai-2026.pdf", "verified", CHECKED + " An expired licence is not exchanged, and a digital licence is not exchanged."),
        ],
    },
    "vh02": {
        "steps": [
            "Order the driving-rights certificate from the state that issued the licence. For a Florida licence, that is Florida.",
            "Wait until you are close to the exchange appointment. The Collectivité checklist says the certificate must be under 3 months old, and it needs a translation.",
            "Ask the desk whether that certificate also needs an apostille. That point is still to be confirmed.",
        ],
        "docs": [
            "The state's certificate of driving rights, dated within 3 months of the day you file.",
            "A translation of that certificate.",
        ],
        "verify": "Whether the Collectivité also wants the driving-rights certificate apostilled, or only translated. The checklist PDF says the licence translation must be legalised or apostilled. For the driving-rights certificate it says 'translation' and does not repeat the word apostille. Ask the desk.",
        "links": [
            L("Collectivité checklist (PDF), including the €150 fee", "https://comsaintmartin.cdn.prismic.io/comsaintmartin/ERLUtyH8BYxvPBxg_LISTEECHANGEPERMISETRANGER.pdf", "verified", CHECKED + " The driving-rights line says under 3 months, plus a translation."),
        ],
    },
    "vh04": {
        "alert": FLORIDA_ALERT,
        "fee_line": "Fee: €150 for this exchange, confirmed on the Collectivité checklist PDF on Oct 29, 2026. Pay it after they check the file, by cheque, cash or card. If both of you file, ask whether each file is €150.",
        "steps": [
            "Open the Collectivité checklist PDF and use that list.",
            "For a US licence, the lines that match are: two colour copies of the licence, front and back, plus the original; the residence permit, copy and original; the passport, copy and original; an official French translation of the licence, legalised or apostilled; proof of address under 3 months old; two photos, 35 by 45 mm, grey or blue background; a driving-rights certificate under 3 months old, plus a translation.",
            "The PDF also has lines for European nationals. If a line does not fit a US passport, ask the desk. Do not skip a line they ask for.",
            "The fee is €150, paid after they check the file, by cheque, cash or card. That amount is printed on the checklist.",
        ],
        "docs": [
            "Everything in the PDF list above.",
            "€150 per exchange file, after the checks. If both of you file, ask whether each file is €150. The PDF states 150,00 € for the request.",
            "Proof of address under 3 months old. The visiteur card page uses under 6 months. They are different rules. This file wants under 3 months.",
        ],
        "tips": [
            "The fee is no longer an open question. It is on the Collectivité's own checklist, checked Oct 29, 2026.",
        ],
        "verify": "Whether the driving-rights certificate needs an apostille as well as a translation. And whether a Saint-Martin licence lets you drive in mainland France and the European Union.",
        "links": [
            L("Collectivité checklist (PDF), fee €150", "https://comsaintmartin.cdn.prismic.io/comsaintmartin/ERLUtyH8BYxvPBxg_LISTEECHANGEPERMISETRANGER.pdf", "verified", CHECKED + " The PDF says 150,00 €, paid after the usual checks, by cheque, cash or card."),
            L("Collectivité: exchange a foreign licence", "https://www.com-saint-martin.fr/thematiques/mobilite-et-transport/demarches-permis-de-conduire/demande-dechange-de-permis-de-conduire-etranger", "verified", CHECKED),
        ],
    },
    "v12": {
        "alert": FLORIDA_ALERT,
        "fee_line": "Fee: €150, confirmed on the Collectivité checklist PDF on Oct 29, 2026. The older checklist line said €150 each. Pay after they check the file, by cheque, cash or card.",
        "steps": [
            "Call 0590 87 61 91 before you go. Opening hours were not on the pages checked Oct 29, 2026. An older Scout note says Monday to Friday 8:15 a.m. to 1:00 p.m. Confirm that.",
            "Hand in the folder at Service des titres de circulation, 7 rue Victor Maurasse, Marigot, 97801.",
            "They take the foreign licence. Pay €150 after they check the file.",
            "Ask whether the Saint-Martin licence is valid for driving in mainland France and the European Union. That answer is still to be confirmed.",
        ],
        "docs": [
            "The folder from the checklist PDF.",
            "€150, after they accept the file. Cheque, cash or card.",
            "Your residence permit. The exchange page says you need it.",
        ],
        "verify": "Opening hours, and whether a Saint-Martin licence is accepted in mainland France and the European Union.",
        "links": [
            L("Collectivité: exchange a foreign licence", "https://www.com-saint-martin.fr/thematiques/mobilite-et-transport/demarches-permis-de-conduire/demande-dechange-de-permis-de-conduire-etranger", "verified", CHECKED),
            L("Collectivité checklist (PDF), fee €150", "https://comsaintmartin.cdn.prismic.io/comsaintmartin/ERLUtyH8BYxvPBxg_LISTEECHANGEPERMISETRANGER.pdf", "verified", CHECKED),
        ],
    },
    "it04": {
        "steps": [
            "Open the Collectivité page on tax residence and the 5-year rule.",
            "That rule is aimed at people coming from mainland France or a French overseas department. The same page also tells foreign nationals living in Saint-Martin to establish their tax residence.",
            "Open the Saint-Martin tax office guide. It says the only tax treaty Saint-Martin has signed is with the French state, and that the tax treaties signed by France do not apply in Saint-Martin.",
            "This is background for your preparer. It is not tax advice.",
        ],
        "docs": [
            "The three Collectivité tax pages already linked on this step, plus the 2021 Doing Business guide linked below.",
        ],
        "tips": [
            "The guide is dated 2021. The sentence on treaties is in the section on the tax environment. A preparer should say whether anything newer has changed it.",
        ],
        "verify": "How the 5-year rule applies to people arriving from the United States, and how Saint-Martin taxes US Social Security. Ask the tax office and your preparer. The treaty question itself is on the next steps.",
        "links": [
            L("Collectivité: tax residence and the 5-year rule", "https://www.com-saint-martin.fr/thematiques/impots-et-fiscalite/fiscalite-pour-les-particuliers/residence-fiscale-a-saint-martin---la-regle-des-5-ans", "verified", CHECKED + " Page updated April 29, 2026."),
            L("Saint-Martin tax office guide, 2021 (PDF)", "https://www.impots-saint-martin.fr/files/file/News/2022/Doing%20Business%202021.pdf", "verified", CHECKED + " Says France's tax treaties do not apply in Saint-Martin, and that the only treaty signed is with the French state."),
        ],
    },
    "it05": {
        "steps": [
            "Call or email the tax office in Concordia. The phone and address are in the contact card.",
            "Ask when two people arriving from the United States become tax residents, and how Saint-Martin taxes US Social Security.",
            "There is no separate filing deadline just for the residence question. Settle it before you file a return.",
            "This call is not tax advice. Write down what they say and take it to your preparer.",
        ],
        "docs": [
            "Your questions, written down.",
            "No fee is listed for asking.",
            "Office hours were not on the page. To be confirmed when you call 0590 29 25 71.",
        ],
        "verify": "How the 5-year rule applies to arrivals from the United States, and the Saint-Martin tax treatment of US Social Security and any US pension. The office has to answer that. The treaty reading is on the next step.",
        "links": [
            L("Collectivité: tax residence and the 5-year rule", "https://www.com-saint-martin.fr/thematiques/impots-et-fiscalite/fiscalite-pour-les-particuliers/residence-fiscale-a-saint-martin---la-regle-des-5-ans", "verified", CHECKED),
        ],
    },
    "it06": {
        "steps": [
            "Open the US-France treaty PDF on the IRS site. Article 3 says 'France', in a geographical sense, means the European and overseas departments of the French Republic. There is no clause in that definition for the collectivités.",
            "Article 18(1)(b) says US Social Security paid to a resident of the other country is taxable only in the country that pays it. Article 29(3)(a) says the United States still has to give that benefit to its citizens. Both sentences were read in the treaty PDF on Oct 29, 2026.",
            "That protection applies to a resident of France as the treaty defines France. Saint-Martin stopped being part of the department of Guadeloupe in 2007.",
            "The Saint-Martin tax office guide (2021) says the tax treaties signed by France do not apply in Saint-Martin, and that Saint-Martin's only treaty is with the French state. Saint-Martin rules still allow a credit for tax withheld abroad even without a treaty.",
            "France and Saint-Martin have their own tax convention. That is a different document from the US treaty. The BOFiP page opened on Oct 29, 2026.",
            "Take this to a preparer. The reading points to the US treaty not covering Saint-Martin. The preparer has to confirm it. This is not tax advice.",
        ],
        "docs": [
            "The treaty PDF and the Saint-Martin guide, saved so you can show the preparer.",
            "These questions for the preparer: Does the US-France treaty apply to a Saint-Martin resident at all? How does Saint-Martin tax US Social Security, pensions and IRA income, and at what rates? Can a Saint-Martin tax on Social Security be claimed on US Form 1116, and how far does it offset the US tax? When do you become Saint-Martin tax residents, and what do you file in the first year? If either of you works, does the US-France social security totalization agreement cover Saint-Martin? What is your state tax status, Florida or Indiana, for the year you move?",
        ],
        "tips": [
            "If Saint-Martin taxes the benefits and the US taxes them too, the US foreign tax credit is the relief the research note points to. Your preparer has to say whether it fits. Not tax advice.",
            "No deadline falls on November 19. Book the preparer before the move, because Saint-Martin residence starts the clock.",
        ],
        "verify": "The six preparer questions in the 'what to have ready' list. The treaty text and the Saint-Martin tax office guide both point to the US treaty not applying. That is a reading for your preparer to confirm, not a tax opinion from this app.",
        "links": [
            L("IRS: US-France treaty text (PDF)", "https://www.irs.gov/pub/irs-trty/france.pdf", "verified", CHECKED + " Articles 3, 18(1)(b) and 29(3)(a) were read in this file."),
            L("IRS: US-France treaty documents", "https://www.irs.gov/businesses/international-businesses/france-tax-treaty-documents", "verified", CHECKED),
            L("Saint-Martin tax office guide, 2021 (PDF)", "https://www.impots-saint-martin.fr/files/file/News/2022/Doing%20Business%202021.pdf", "verified", CHECKED),
            L("BOFiP: tax convention between France and Saint-Martin", "https://bofip.impots.gouv.fr/bofip/2607-PGP.html/identifiant%3DBOI-INT-CVB-MAF-20120912", "verified", CHECKED),
            L("IRS: foreign tax credit", "https://www.irs.gov/individuals/international-taxpayers/foreign-tax-credit", "verified", CHECKED),
            L("IRS Publication 915: Social Security and tax", "https://www.irs.gov/publications/p915", "verified", CHECKED),
        ],
    },
    "wk7": {
        "verify": "Whether the US-France social security totalization agreement covers Saint-Martin. This only matters if either of you works. Ask your preparer. Not tax advice.",
    },
}

TIMELINE = (
    "Your lease end in the app is still November 19, 2026. You do not have to file the long-stay visa before that date. "
    "You can apply from Indiana. Chicago is the nearest visa centre. Washington, DC decides every US application, and you may use any of the 11 centres. "
    "File no earlier than 3 months before the departure date you choose, book the centre at least 1 month ahead, and allow at least 15 days for a decision. "
    "Before November 19, while you still have a Florida address, order apostilled birth and marriage records, keep your Florida driving licences valid, and do not switch them to Indiana licences. "
    "Without the long-stay visa you can enter for up to 90 days in any 180, but you cannot settle or switch to residence there. You would go back to the United States to apply. "
    "This is planning help, not immigration or tax advice."
)

QUESTIONS = [
    "What departure date will you use for the visa? You can file no earlier than 3 months before that date. November 19, 2026 does not have to be the filing deadline.",
    "Will either of you work remotely after the move? That changes the visa and the tax steps.",
    "Is either of you on Medicare now, or turning 65 soon? A yes or no is enough. Medicare generally does not pay for care outside the United States.",
    "Will you own a car in Saint-Martin, or rent for a long time?",
    "Which state is printed on each current driving licence? Keep Florida licences. Do not switch to Indiana.",
    "Social Security: keep a US bank account. A euro deposit at a Saint-Martin bank is not confirmed. Ask SSA before you close the US account.",
]


def apply_contacts(contacts):
    contacts["ssa"] = {
        "title": "Social Security from Saint-Martin",
        "lines": [
            "French Saint-Martin is not named on SSA's country list. Do not assume Paris.",
            "The same list sends Guadeloupe, Saint-Barthélemy, Sint Maarten (Dutch side) and Martinique to the Federal Benefits Unit at the US Embassy in Santo Domingo: Av. República de Colombia #57. Phone 809-368-7011. Fax 809-922-7001. Email FBU.Santo.Domingo@ssa.gov. That reading is from the Oct 29 research note. The page blocked an automatic check in this pass. Open it in Chrome.",
            "The Santo Domingo unit's own page says it serves the Caribbean islands and Colombia. It does not name French Saint-Martin. That page opened on Oct 29, 2026.",
            "Ask by email at FBU.Santo.Domingo@ssa.gov, or call SSA at 1-800-772-1213, before you move. Which office serves French Saint-Martin is still to be confirmed.",
            "In May 2023 that unit held visits at 21 Rue de la Petit Plage, Grand Case 97150, on the French side. Appointments were by the same email.",
            "The simplest payment plan is to keep a US bank account. A deposit into a Saint-Martin euro account is still to be confirmed.",
        ],
        "source": "SSA foreign-office list (open in Chrome), US Embassy Santo Domingo, and the May 5, 2023 Bridgetown notice. Checked Oct 29, 2026.",
        "url": "https://do.usembassy.gov/social-security/",
        "tel": "+18007721213",
    }
    contacts["cgss"]["lines"] = [
        "Accueil Maladie, Spring Concordia, 6 rue Jean-Luc Hamlet, 97150 Saint-Martin.",
        "Front desk, from the official directory: Monday, Tuesday and Thursday 7:30 a.m. to noon. Wednesday and Friday 8:00 a.m. to noon.",
        "Phone 36 46. From the US: +33 1 84 90 36 46.",
        "Book from an ameli account, or by calling 36 46.",
        "Postal address for the file: Assurance Maladie, CS 48105, 97181 Les Abymes Cedex (Guadeloupe).",
        "The directory was last changed March 28, 2024, and it opened again on Oct 29, 2026.",
        "Hours printed as 7:30 a.m. to 11:00 a.m. on that page are the relay for deaf and hard-of-hearing people, not the front desk.",
        "The Guadeloupe CGSS website was down on Oct 29, 2026. A search snippet showed different hours. Ignore the snippet and confirm when you call.",
    ]
    contacts["titres"]["lines"] = [
        "7 rue Victor Maurasse, Marigot, 97801 Saint-Martin.",
        "Phone 0590 87 61 91. From the US: +590 590 87 61 91.",
        "Email servicedestitres@com-saint-martin.fr.",
        "Fee on the Collectivité checklist PDF, checked Oct 29, 2026: €150, paid after they check the file, by cheque, cash or card.",
        "Opening hours were not on the pages checked that day. An older Scout note says Monday to Friday 8:15 a.m. to 1:00 p.m. To be confirmed. Call first.",
        "A Florida licence can be exchanged for categories A and B. An Indiana licence cannot. Keep the Florida licences.",
    ]
