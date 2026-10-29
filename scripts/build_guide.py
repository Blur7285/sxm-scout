#!/usr/bin/env python3
"""Build guide-data.js from the approved checklist plus sourced extras.

Does not invent official URLs. Link states come from the 29 Oct 2026 recheck.
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC = pathlib.Path(__file__).resolve().parents[1] / "data" / "checklists-v1.json"
OUT = ROOT / "guide-data.js"
LINK_LOG = pathlib.Path(__file__).resolve().parents[1] / "data" / "linkcheck-2026-10-29.tsv"

# Retries after the first pass.
OVERRIDES = {
    "https://www.hcch.net/en/instruments/conventions/authorities1/?cid=41": (
        "verified",
        "Opened OK on a second try on Oct 29, 2026 (the first try timed out).",
    ),
    "https://fam.state.gov/fam/07fam/07fam0530.html": (
        "flagged",
        "Could not re-open this page on Oct 29, 2026: the certificate check failed. It had opened on Oct 28, 2026. Open it in Chrome. Not replaced.",
    ),
    "https://www.hcch.net/en/instruments/conventions/specialised-sections/apostille": (
        "flagged",
        "Timed out on Oct 29, 2026, so this address was not re-confirmed. It had opened on Oct 28, 2026. Open it in Chrome. Not replaced.",
    ),
}


def load_link_states():
    states = {}
    for line in LINK_LOG.read_text().splitlines():
        if not line.strip():
            continue
        left, url = line.split("\t", 1)
        parts = left.split(" ", 1)
        code = parts[0]
        final = parts[1] if len(parts) > 1 else url
        if url in OVERRIDES:
            states[url] = {"state": OVERRIDES[url][0], "detail": OVERRIDES[url][1], "final": final}
            continue
        if code == "200":
            detail = "Opened OK on Oct 29, 2026."
            if final.rstrip("/") != url.rstrip("/") and not final.startswith(url):
                detail += " It redirected to " + final + "."
            elif final.rstrip("/") != url.rstrip("/"):
                detail += " It redirected to " + final + "."
            states[url] = {"state": "verified", "detail": detail, "final": final}
        elif code == "403":
            states[url] = {
                "state": "flagged",
                "detail": "The site blocked an automatic check on Oct 29, 2026 (not a dead page). This is still the official address. Open it in Chrome.",
                "final": final,
            }
        else:
            states[url] = {
                "state": "flagged",
                "detail": "Could not confirm this address on Oct 29, 2026 (result " + code + "). Open it in Chrome. Not replaced.",
                "final": final,
            }
    return states


CONTACTS = {
    "emergency": {
        "title": "Emergency numbers",
        "lines": [
            "15 medical emergency, 17 police, 18 fire, 112 any emergency.",
            "Save them in both phones before you fly.",
        ],
        "source": "service-public.fr page F33954 (emergency numbers). The page opened on Oct 29, 2026. The meanings above are the ones in the approved step.",
        "url": "https://www.service-public.gouv.fr/particuliers/vosdroits/F33954",
    },
    "hospital": {
        "title": "Louis-Constant Fleming hospital",
        "lines": [
            "Address on Santé.fr: Rue Louis Constant Fleming, 97150 Saint-Martin.",
            "Main phone on that page: 0590 52 25 25. From the US, dial +590 590 52 25 25.",
            "Emergencies are listed as open 24 hours. For a life-threatening emergency, call 15.",
            "An older Scout page also lists Spring-Concordia, BP 381, and a separate emergency line 0590 52 25 52. Those were not on the Santé.fr page checked Oct 29, 2026. To be confirmed.",
        ],
        "source": "Santé.fr hospital page, checked Oct 29, 2026.",
        "url": "https://www.sante.fr/centre-hospitalier-ch/saint-martin/centre-hospitalier-louis-constant-fleming",
        "tel": "+590590522525",
    },
    "cgss": {
        "title": "CGSS desk in Marigot (health office)",
        "lines": [
            "Accueil Maladie, Spring Concordia, 6 rue Jean-Luc Hamlet, 97150 Saint-Martin.",
            "Hours on the official directory: Monday and Tuesday 7:30 a.m. to noon, Wednesday 8:00 a.m. to noon, Thursday 7:30 a.m. to noon, Friday 8:00 a.m. to noon.",
            "Phone 36 46. From the US: +33 1 84 90 36 46.",
            "Book a visit from an ameli account, or by calling 36 46.",
            "Postal address for the file: Assurance Maladie, CS 48105, 97181 Les Abymes Cedex (Guadeloupe).",
            "The directory page says it was last modified March 28, 2024. Call before you go, in case the hours changed.",
        ],
        "source": "Annuaire service-public, CGSS Saint-Martin page, checked Oct 29, 2026.",
        "url": "https://lannuaire.service-public.gouv.fr/collectivites-d-outre-mer/saint-martin/635a7d03-af7b-4cca-8f8b-1c28d5c6d692",
        "tel": "+33184903646",
    },
    "prefecture": {
        "title": "Préfecture (immigration)",
        "lines": [
            "Cité administrative, 23 rue de Spring, Concordia, 97150 Saint-Martin.",
            "Phone +590 590 52 30 50. Email contact@saint-barth-saint-martin.gouv.fr.",
            "Hours saved in Scout from this office's page on Oct 26, 2026: Monday, Tuesday and Thursday 8:30 a.m. to noon and 2:00 p.m. to 4:00 p.m. Wednesday and Friday 8:30 a.m. to noon.",
            "Immigration appointments are booked online. A walk-in was listed only for récépissé renewals, Wednesday 8:30 to 9:30 a.m.",
            "To be confirmed: the hours page would not open on Oct 29, 2026 (the site closed the connection). Call before you go.",
        ],
        "source": "Préfecture hours page, as recorded in Scout on Oct 26, 2026. Not re-read on Oct 29, 2026.",
        "url": "https://www.saint-barth-saint-martin.gouv.fr/Outils/Horaires-et-coordonnees",
        "tel": "+590590523050",
    },
    "tax": {
        "title": "Saint-Martin tax office",
        "lines": [
            "Centre des finances publiques de Saint-Martin, 16 rue Jean-Jacques Fayel, Concordia, 97150 Saint-Martin.",
            "Individuals: 0590 29 25 71. Email cfip.sxm.servicedesparticuliers@dgfip.finances.gouv.fr.",
            "From the US, dial +590 590 29 25 71.",
            "Office hours were not on the page. To be confirmed when you call.",
        ],
        "source": "Collectivité tax-residence page (contact block), page updated April 29, 2026, checked Oct 29, 2026.",
        "url": "https://www.com-saint-martin.fr/thematiques/impots-et-fiscalite/fiscalite-pour-les-particuliers/residence-fiscale-a-saint-martin---la-regle-des-5-ans",
        "tel": "+590590292571",
    },
    "titres": {
        "title": "Service des titres de circulation",
        "lines": [
            "7 rue Victor Maurasse, Marigot, 97801 Saint-Martin.",
            "Phone 0590 87 61 91. From the US: +590 590 87 61 91.",
            "Email servicedestitres@com-saint-martin.fr.",
            "Opening hours were not on the pages checked Oct 29, 2026. An older Scout note says Monday to Friday 8:15 a.m. to 1:00 p.m. To be confirmed. Call first.",
        ],
        "source": "Collectivité pages for licence exchange (updated Sept 9, 2026) and vehicle registration, checked Oct 29, 2026.",
        "url": "https://www.com-saint-martin.fr/thematiques/mobilite-et-transport/demarches-permis-de-conduire/demande-dechange-de-permis-de-conduire-etranger",
        "tel": "+590590876191",
    },
    "adil": {
        "title": "ADIL (free housing advice)",
        "lines": [
            "5 rue Léopold Mingau, Concordia, 97150 Saint-Martin.",
            "Phone 0590 29 13 10. From the US: +590 590 29 13 10.",
            "Email listed on the Collectivité page: swendie.hanson@com-saint-martin.fr.",
            "Opening hours were not on that page. To be confirmed when you call.",
        ],
        "source": "Collectivité ADIL page, checked Oct 29, 2026.",
        "url": "https://www.com-saint-martin.fr/thematiques/habitat-foncier-et-urbanisme/se-loger-a-saint-martin/agence-departementale-dinformaiton-sur-le-logement-adil",
        "tel": "+590590291310",
    },
    "edf": {
        "title": "EDF, Saint-Martin",
        "lines": [
            "Address in Scout: Route de La Colombe, Concordia, 97150.",
            "Phone 0590 87 50 30. From the US: +590 590 87 50 30. Scout also lists 0590 82 43 00 outside office hours.",
            "Hours in Scout: front desk Monday and Wednesday 7:30 a.m. to noon. Phone Monday to Thursday 7:30 a.m. to 2:00 p.m., Friday 7:30 a.m. to 1:00 p.m.",
            "To be confirmed. The EDF contact page blocked the automatic check on Oct 29, 2026, and Scout already said the agency has used shorter hours.",
        ],
        "source": "EDF contact page linked below (blocked to an automatic check). Hours are from Scout's lease page, last written there Oct 26, 2026.",
        "url": "https://www.edf.gp/particulier/mon-agence/contact-0",
        "tel": "+590590875030",
    },
    "eeasm": {
        "title": "Water: EEASM and SAUR",
        "lines": [
            "EEASM office: Immeuble KAKI, 9 rue Barbuda, ZAC Hope Estate II, 97150 Saint-Martin.",
            "Public desk listed on eeasm.org: Wednesday 8:00 a.m. to 2:00 p.m. and Thursday 8:00 a.m. to 2:00 p.m.",
            "The company that runs the service (SAUR Saint-Martin): 5 rue Léopold Mingau, Marigot, 97150. Phone 0590 87 97 03. From the US: +590 590 87 97 03.",
            "EEASM's own phone number was not on the page. To be confirmed. Start with SAUR for a new account.",
        ],
        "source": "eeasm.org footer, checked Oct 29, 2026.",
        "url": "https://www.eeasm.org/",
        "tel": "+590590879703",
    },
    "iedom": {
        "title": "IEDOM (right to a bank account)",
        "lines": [
            "The Guadeloupe agency also covers Saint-Martin and Saint-Barthélemy.",
            "13 boulevard Daniel Marsin, Parc d'activités la Providence, ZAC de Dothémare Sud, 97139 Abymes, Guadeloupe.",
            "Phone 0590 93 74 00 or 0590 93 74 26. Email particuliers-guadeloupe@iedom.fr.",
            "At the Abymes office: Monday, Tuesday, Thursday and Friday, 9:00 a.m. to noon, by appointment only. Bring a current photo ID.",
            "Saint-Martin desk: the first Friday of each month, Collectivité meeting room, rue Victor Maurasse, Marigot 97150.",
            "From the US, dial +590 590 93 74 00.",
        ],
        "source": "IEDOM Guadeloupe page and the droit-au-compte page, checked Oct 29, 2026.",
        "url": "https://www.iedom.fr/Guadeloupe",
        "tel": "+590590937400",
    },
    "laposte": {
        "title": "La Poste, Marigot",
        "lines": [
            "Scout lists 25 rue de la Liberté, 97150 Marigot, phone 0969 397 398.",
            "Hours in that same note: Monday, Tuesday, Thursday and Friday 7:00 a.m. to 1:00 p.m., Wednesday 8:00 a.m. to 1:00 p.m., Saturday 7:00 a.m. to 12:30 p.m.",
            "To be confirmed. Scout says those figures came from an aggregator, not from La Poste's own page. La Poste's site blocked the automatic check on Oct 29, 2026.",
        ],
        "source": "Scout Mail page, last written Oct 26, 2026. Not re-confirmed from laposte.fr.",
        "url": "https://www.laposte.fr/",
    },
    "embassy": {
        "title": "US Embassy Bridgetown",
        "lines": [
            "This is the post Scout lists for US citizens on the French side, not the consulate that covers Dutch Sint Maarten.",
            "Wildey Business Park, Wildey, St. Michael BB14006, Barbados.",
            "Phone +1 246 227-4399. After-hours emergency +1 246 227-4000. Email BridgetownACS@state.gov.",
            "To be confirmed on the embassy site before you rely on the numbers. The home page opened on Oct 29, 2026. The numbers are the ones already printed in Scout, which asked you to confirm them.",
        ],
        "source": "Scout consular page, and bb.usembassy.gov (home page opened Oct 29, 2026).",
        "url": "https://bb.usembassy.gov/",
        "tel": "+12462274399",
    },
    "ssa": {
        "title": "Social Security from Saint-Martin",
        "lines": [
            "Which US office handles French Saint-Martin is not settled.",
            "A State Department table (7 FAM 537) puts Guadeloupe, Saint-Barthélemy and Sint Maarten under Santo Domingo. It does not name French Saint-Martin.",
            "SSA's direct-deposit country list names France and Martinique. It does not name Saint-Martin.",
            "An older Scout note says to mail form SSA-1199-FR to the Federal Benefits Unit at the US Embassy in Paris. Do not assume Paris is the right office until SSA says so.",
            "Ask SSA, and write down the answer. To be confirmed.",
        ],
        "source": "Gaps noted Oct 28, 2026 from the FAM table and SSA's country list. The FAM page could not be re-opened on Oct 29, 2026 (certificate check failed).",
        "url": "https://fam.state.gov/fam/07fam/07fam0530.html",
    },
    "visafees": {
        "title": "Fees named on service-public (visiteur card)",
        "lines": [
            "Checked on service-public.fr F302 on Oct 29, 2026: at least €1,477.93 net a month for one person (€17,735.19 a year).",
            "Same page: €350 for the first temporary visiteur card (€300 tax + €50 stamp), €250 where that page describes the renewal, and €180 extra if you file late.",
            "The page does not name Saint-Martin. Whether the préfecture charges the same amounts is to be confirmed.",
            "How the €1,477.93 figure works for a couple is also to be confirmed. The page states it for one person.",
        ],
        "source": "service-public.fr F302, checked Oct 29, 2026.",
        "url": "https://www.service-public.gouv.fr/particuliers/vosdroits/F302",
    },
}

# Which contact cards to show on each item. Category defaults are applied first.
CAT_CONTACTS = {
    "healthcare": [],
    "banking": [],
    "civil-records": [],
    "income-tax": [],
    "legal": ["visafees"],
    "housing": [],
    "vehicles": ["titres"],
    "mail": [],
    "phones": [],
    "leaving-home": [],
    "safety-consular": [],
}

ITEM_CONTACTS = {
    "h13": ["hospital", "emergency"],
    "hc01": ["cgss"],
    "hc02": ["cgss"],
    "hc03": ["cgss"],
    "hc04": ["cgss"],
    "hc05": ["cgss"],
    "hc06": ["cgss"],
    "hc07": ["cgss"],
    "h14": ["cgss"],
    "h16": ["cgss"],
    "b15": ["iedom"],
    "it01": ["ssa"],
    "it02": ["ssa"],
    "mv_ssa": ["ssa"],
    "b16": ["ssa"],
    "it03": ["ssa"],
    "it04": ["tax"],
    "it05": ["tax"],
    "it06": ["tax"],
    "tx6": ["tax"],
    "tx7": ["tax"],
    "wk7": ["tax"],
    "ld34": ["prefecture"],
    "im02": ["prefecture"],
    "ld35": ["prefecture", "visafees"],
    "ld37": ["prefecture", "tax", "ssa"],
    "mw_3": ["prefecture"],
    "ld31": ["prefecture"],
    "hs04": ["adil"],
    "l5": ["adil"],
    "l12": ["adil"],
    "hs02": ["adil"],
    "hs03": ["adil"],
    "hs05": ["edf"],
    "hs06": ["eeasm"],
    "hs07": ["adil", "tax"],
    "vh04": ["titres"],
    "v12": ["titres"],
    "v11": ["titres"],
    "vh07": ["titres"],
    "vh05": ["titres"],
    "ml03": ["laposte"],
    "ml04": ["laposte"],
    "ml05": ["prefecture", "titres"],
    "sc03": ["emergency", "hospital"],
    "sc02": ["embassy"],
    "sc04": ["embassy"],
    "pt01": [],
}

# Documents, numbers and fees that are not already a phone/address card.
DOCS = {
    "h4": ["Age of each person to cover.", "The arrival date you want cover to start.", "A list of what the quote must include: doctor visits, specialists, prescriptions, hospital, evacuation, and any health condition you already have."],
    "h5": ["Quote A, so you can compare.", "The same ages, date and coverage list you used for quote A."],
    "h6": ["The policy wording PDF for the plan you picked, not the sales brochure.", "A list of health conditions you need the insurer to answer in writing. Keep the medical detail in the insurer's email, not in this notes box."],
    "h8": ["The insurer's certificate (attestation), in French or English.", "It should show every name, the start and end dates, Saint-Martin (French side), and amounts in euros.", "A printed copy for the visa folder and a PDF saved offline.", "The exact wording the consulate wants is still to be confirmed. Check the France-Visas document list when you build the file."],
    "h9": ["Your flight date.", "The end date of any travel policy, so the new policy starts before that one ends."],
    "h7": ["Whether the health plan already includes evacuation.", "One written price for an evacuation membership if it does not."],
    "h1": ["Appointments with your current doctor, dentist and eye doctor.", "Paper copies of records and recent tests in your carry-on, plus a cloud copy.", "Do not put diagnoses or medicine names in the notes box if you can avoid it. Write 'records saved' instead."],
    "h10": ["The policy PDF, the card, and the claims phone number, saved so they open with no internet.", "One printed set in the document bag."],
    "hc01": ["Nothing to sign yet. You are only reading the rules.", "A note of the 3-month and 6-month rules, and whether the new payment for people who do not work has been published. That payment amount is to be confirmed."],
    "hc02": ["The day you arrived in Saint-Martin.", "A calendar reminder for 3 months after that day. Cover does not open before then."],
    "hc03": ["Passport for each person.", "Proof you are allowed to stay (visa or residence paper).", "Proof of address.", "Birth certificates. Whether they must be apostilled and translated for this file is to be confirmed with the CGSS desk.", "The exact document list the Marigot desk wants is to be confirmed. Ask them before you mail anything."],
    "hc04": ["The finished PUMa file.", "An appointment. Do not count on walking in. Hours are mornings only, in the contact card below."],
    "hc05": ["A copy of everything you hand in.", "Proof of mailing if you send it (the checklist allows a few euros for a registered letter).", "The postal address in Les Abymes, from the contact card."],
    "hc06": ["The social security number, once CGSS sends it. How long Saint-Martin files take is to be confirmed.", "An email address you can open for the ameli account.", "Do not type the social security number into the notes box."],
    "hc07": ["Your social security number and ameli login.", "A French postal address.", "Whether the phone app (digital carte Vitale) is offered in Saint-Martin is to be confirmed."],
    "h14": ["Your social security number.", "The name of the doctor you want as médecin traitant.", "The declaration form the doctor gives you, or the online declaration on ameli."],
    "h16": ["A list of what PUMa does not pay, from the ameli or mutuelle quote.", "Prices from two top-up plans. Complémentaire santé solidaire is only for people under an income limit. Check the official page before you assume you qualify."],
    "h13": ["Both phones, so you can save the numbers below.", "The hospital address. Use the Santé.fr address. The older BP 381 line is to be confirmed."],
    "hc10": ["Nothing to cancel. This step is reading only.", "Medicare's own page on care outside the United States."],
    "hc11": ["Your Medicare letters, or a login to Medicare.gov. Do not type the Medicare number here.", "A question list for SSA or Medicare: the penalty if you drop Part B, and the dates you could sign up again. Those numbers are personal. To be confirmed with SSA. Do not cancel anything on this step."],
    "hc12": ["The name of any Advantage, Part D or Medigap plan.", "That plan's own rule for members who move abroad. Each plan is different. To be confirmed with the plan."],
    "b14": ["Your bank's secure message or phone number, from the back of your card.", "Ask if a Saint-Martin address is allowed. Get the answer in writing if you can. Some US banks limit accounts with a foreign address. To be confirmed with your bank."],
    "b1": ["Each card you will use on the trip.", "The bank's travel-notice or international-use switch, in the bank app or by phone."],
    "b2": ["The fee list for each card: foreign transaction fee, and ATM fees.", "Keep the card that charges no foreign fee, if you have one."],
    "b3": ["A Wise account (or another multi-currency account).", "A small test amount you can afford to send.", "The euro details the landlord would use later. Do not type full account numbers in the notes box. Write 'test sent' and the date."],
    "b4": ["An authenticator app on each phone, plus backup codes stored offline.", "A check that the bank is not using only your US text messages for sign-in."],
    "b5": ["A short list of 2 or 3 banks. Scout names BRED, Caisse d'Epargne CEPAC, Crédit Mutuel, LCL, and La Banque Postale (25 rue de la Liberté) as banks people use. Which ones are taking new personal customers is to be confirmed.", "Passport, and a question list: US citizen rules, appointment or not, and what they need for proof of address."],
    "bk01": ["IRS Form W-9, from the IRS page linked below.", "Your US tax number, which you fill in on the form at the bank. Do not type it in the notes box."],
    "b6": ["Passport.", "Visa or residence paper.", "Proof of address.", "Proof of income (Social Security letter).", "The W-9 from the step above."],
    "b8": ["The document folder from the step above.", "An appointment if the bank asked for one.", "When you leave, a RIB (the sheet with your IBAN). Photograph it. Do not paste the full IBAN into notes if you can keep the photo instead."],
    "b15": ["A written refusal from the bank, if they say no. The droit au compte process asks for that letter.", "Photo ID.", "The IEDOM form from the page linked below. The service is free."],
    "b7": ["Your IBAN (on the RIB) or the Wise euro details.", "The landlord's preferred method, written into the lease or an email."],
    "b9": ["The new card and PIN.", "A small shop payment and one ATM withdrawal. Write the date in notes, not the PIN."],
    "bk02": ["The highest total your foreign accounts reached in the year. You need this later for the FBAR.", "The IRS FBAR page, to check this year's deadline. The deadline is to be confirmed on that page each year. Do not type account numbers here."],
    "bk03": ["The same foreign-account totals, in US dollars.", "Form 8938's instructions, to see if you are over the limit for people living abroad."],
    "ld1": ["Both passports.", "Check the expiry date, blank pages, and that the passport was issued less than 10 years ago.", "The renewal fee is on the State Department fee list. The renewal page blocked an automatic check. Open it in Chrome."],
    "cr01": ["The state or county that holds each birth record and the marriage record.", "The CDC 'where to write for vital records' page lists the office for each state. It blocked an automatic check. Open it in Chrome."],
    "cr02": ["The question, asked in writing: how recent must a US certificate be for the visa, and for the préfecture? A 3-month or 6-month limit is to be confirmed."],
    "ld17": ["The issuing office's order form, for each adult.", "A full certified copy, with the latest mentions, not a short abstract.", "The fee is set by that office. To be confirmed on their form.", "Allow weeks."],
    "ld18": ["The issuing office for the marriage record. Skip this step if you are not married.", "Fee: set by that office. To be confirmed."],
    "cr03": ["The state that issued each certificate. The apostille comes from that same state.", "The Hague Conference list of US apostille authorities. If a record is from a country that is not in the Apostille Convention, it needs legalisation instead. See service-public F1402."],
    "ld19": ["The certified birth certificate.", "Payment for that state's apostille. The fee varies. To be confirmed on the state site.", "A tracked envelope back to you."],
    "ld19m": ["The certified marriage certificate.", "The same state's apostille fee. To be confirmed on the state site."],
    "ld20": ["The apostilled originals, stored flat. Not in checked luggage.", "A scan of each one in cloud storage."],
    "ld24": ["A written answer: which papers need a sworn French translation for the visa, and which for the préfecture and the CGSS. To be confirmed with France-Visas and the préfecture.", "Do not pay for a translation until you have that answer."],
    "cr04": ["The list of approved translators from the Court of Appeal of Basse-Terre (it covers Saint-Martin).", "A quote per page. The checklist says to ask for a quote. There is no set price here."],
    "cr05": ["The originals or good scans, as the translator asks.", "The quote you accepted.", "A date you need them back, before the visa appointment."],
    "ld21": ["Do not order an FBI check until you know you need one. It was not on the official lists checked for a visiteur visa.", "If they ask: FBI Identity History Summary, then a federal apostille from the State Department, not a state office. Both of those pages blocked an automatic check."],
    "ld13": ["Every original, scanned.", "One paper set in the carry-on. Nothing that exists only in checked luggage."],
    "it01": ["A my Social Security login. The page blocked an automatic check.", "The question for SSA: do you treat French Saint-Martin like France for payments abroad? Saint-Martin is not named on the tool. To be confirmed."],
    "it02": ["A benefit-verification letter downloaded from my Social Security, for each person who receives it.", "A PDF saved offline. It is part of the visa proof-of-income file."],
    "mv_ssa": ["Your new address, once you have it. Until then, tell SSA you are moving and ask which office to write to.", "Do not send the Paris mailing from the older Scout note until SSA confirms the office. To be confirmed."],
    "b16": ["A decision: US account or euro IBAN.", "If euro: form SSA-1199-FR. The bank fills in section 3. The form page blocked an automatic check.", "Ask SSA if an IBAN from a Saint-Martin branch is accepted. France is on the direct-deposit list. Saint-Martin is not named. To be confirmed.", "If you already ticked the older banking line about this form, that tick is still on the earlier banking checklist. This line is the newer one."],
    "it03": ["A reminder, once a year, to watch for SSA questionnaires.", "If a letter goes to an old address, payments can stop. This is why the mail steps matter."],
    "tx1": ["Two or three names of preparers who know US citizens abroad and Saint-Martin's own tax.", "A first-call date. No government fee for this step."],
    "tx2": ["A list of income types only: Social Security, any job, interest, dividends. Do not type amounts or account numbers in the notes box unless you are comfortable with them sitting in the sync file."],
    "it04": ["The three Collectivité pages linked below.", "The 5-year rule, as that page describes it, is aimed at people coming from mainland France or a French overseas department. You are coming from the United States. Ask how it applies to you. To be confirmed."],
    "it05": ["A call or email to the tax office in the contact card.", "The question: when do we become tax residents, and how is US Social Security taxed here?", "No fee is listed for asking.", "Hours: to be confirmed. The phone is in the contact card."],
    "it06": ["The IRS page of US-France treaty documents, and the treaty PDF.", "The question for your preparer: the treaty text defines France as the European and overseas departments. Saint-Martin has been a collectivity, not a department, since 2007. Does the treaty cover it?", "If it does not, US Social Security might be taxed in both places, and the US foreign tax credit matters. To be confirmed by a preparer. This app is not tax advice."],
    "it07": ["Form 1116's IRS page.", "Any Saint-Martin tax you actually paid. You cannot claim the credit for tax you have not paid."],
    "tx6": ["The US filing date. Citizens abroad get an automatic 2-month extension, to June 15, on the IRS page linked below. You still owe interest on tax not paid by April.", "A calendar entry. Saint-Martin income-tax returns are due May 31 for the year before, on the Collectivité page updated April 29, 2026. Provisional payments are due February 15 and May 15. That is a different return from the US one."],
    "it08": ["The name of the last US state you lived in.", "That state's rule for people who leave. To be confirmed with the preparer or that state's tax office. No single federal page covers every state."],
    "tx7": ["Form 8822 from the IRS page.", "Your Saint-Martin address. Do this after you have one.", "A copy of what you mailed."],
    "tx5": ["A written note of what the preparer said, before you apply for the visa.", "Keep their email. A short reminder in the notes box is enough."],
    "wk7": ["Only if one of you will work. If neither of you will work, mark this done and write 'not working'.", "The question: tax and social charges on that pay, and whether the US-France social security agreement covers Saint-Martin. To be confirmed."],
    "ld12": ["A decision you both sign and date: long-stay visa, or short visits only.", "If the move is still tied to the current lease end (Nov 19, 2026), read the yellow note at the top of Step-by-step. A long-stay visa is applied for before you leave."],
    "ld39": ["The question in writing: can a visiteur do remote work for a foreign employer?", "An older Scout note says the Interior Ministry answered a parliamentary question on June 23, 2026, and that the tax office has not said the same thing. Get a current answer. To be confirmed. This app is not immigration advice."],
    "im01": ["The France-Visas wizard. The page blocked an automatic check. Open it in Chrome.", "Destination: Saint-Martin, not mainland France. Saint-Martin is outside the Schengen area."],
    "ld5": ["The Social Security benefit letter.", "Recent bank statements.", "The €1,477.93 figure is for one person, from F302, checked Oct 29, 2026. How a couple is counted, and whether the gross or net benefit is used, is to be confirmed."],
    "ld6": ["The insurance certificate from the health step.", "Check the names, dates, Saint-Martin, and euro amounts again."],
    "ld7": ["A lease, or a hosting letter from the person you will stay with.", "The card renewal later wants proof of address under 6 months old, from F302. What the visa file wants may differ. To be confirmed on your France-Visas checklist."],
    "ld25": ["A handwritten, signed statement that you will not work in France, one for each adult.", "The exact wording the consulate wants is to be confirmed. Ask them before the appointment. Pen and paper, not a typed page, unless they say typed is fine."],
    "ld27": ["A France-Visas account for each adult.", "The printed form and the receipt.", "Passport details. Type them into France-Visas, not into this notes box.", "Fee: the visa fee is on the France-Visas country page. That page blocked an automatic check. Look at the fee shown there."],
    "ld28": ["The TLScontact page for US visa centres. It blocked an automatic check.", "The centre that covers the state you live in now. Which centre, and the service fee, are to be confirmed on that site.", "Book at least a month ahead. Applications are not opened more than 3 months before you plan to leave."],
    "ld29": ["The visa sticker in the passport.", "Check the type, the dates, and that the territory includes Saint-Martin (or the wording the consulate told you).", "Whether you receive a VLS-TS or a temporary long-stay visa is to be confirmed when you see the sticker. The renewal path depends on it."],
    "mw_3": ["Something that shows the day you entered French territory.", "You land at SXM, which is on the Dutch side. There is no French passport stamp there. Ask the préfecture what they accept as proof. To be confirmed.", "Keep boarding passes."],
    "ld31": ["Only if the sticker is a VLS-TS. If it is not, follow what the sticker says instead.", "An ANEF account. The ANEF site opened on Oct 29, 2026.", "A card to pay the tax. The amount is shown on ANEF at payment. An older note of about €269 is to be confirmed. Pay what the screen says.", "Whether ANEF accepts a Saint-Martin address is to be confirmed. If it does not, ask the préfecture.", "Do this within 3 months of arrival. Sooner is safer."],
    "ld34": ["Your visa and passport.", "An appointment from the préfecture's online booking page. The booking page opened on Oct 29, 2026.", "Hours and the phone are in the contact card. Hours are to be confirmed."],
    "im02": ["The end date of the visa or card.", "A calendar reminder for 4 months before that date, and another for 2 months before. The renewal window on the card page is between 4 and 2 months before the end."],
    "ld35": ["The document list on F302: passport, birth certificate, proof of address under 6 months, proof of resources, photos, the signed commitment, and the fee.", "Fee on F302, checked Oct 29, 2026: €350 first card. Whether Saint-Martin charges that amount is to be confirmed with the préfecture.", "Whether the whole request is done online at this préfecture is also to be confirmed."],
    "ld37": ["A list of offices: préfecture, SSA, IRS, banks, and the tax office.", "Your new address, spelled the way the landlord writes it, including 97150."],
    "hs01": ["A decision written down: rent first. Buying can wait.", "No office visit for this step."],
    "d1": ["The rental email draft already in the Rentals section of this app.", "Two or three French-side agencies. Send from an email you both can open."],
    "hs02": ["Passport, visa or residence paper, proof of income, and the last tax return if you have one.", "The mainland list of papers a landlord may ask for is on service-public F1169. Whether that list is the rule in Saint-Martin is to be confirmed. Ask the ADIL."],
    "hs03": ["The question for the agency: is a guarantor required?", "Visale is the free state guarantee on visale.fr (the site opened Oct 29, 2026). Whether Visale covers a rental in Saint-Martin is to be confirmed."],
    "d2": ["Dates for the first 2 to 4 weeks.", "A written cancellation policy.", "Do not sign a long lease from this short stay."],
    "l1": ["The draft lease, in French. Ask for a translation or a bilingual copy before you pay anything.", "No deposit until you have read it."],
    "l2": ["The rent, what the charges include, the deposit, and any agency fee, in writing, with due dates.", "Who pays the agency. A typical range is in the Budget screen as an estimate, not a legal cap."],
    "l3": ["A written list: electricity, water, internet, and building charges. Each one marked included or extra."],
    "l4": ["The lease clause about storms: shutters, and what happens to the rent if the home cannot be lived in."],
    "l5": ["The notice period in the lease, and the early-exit clause.", "Whether the 1989 rental law applies in Saint-Martin is to be confirmed. Ask the ADIL. Do not rely on a mainland rule until they say so."],
    "hs04": ["The draft lease.", "An appointment or email to the ADIL. The phone is in the contact card. Hours are to be confirmed.", "This advice is free, on the Collectivité page."],
    "l11": ["A written note of who pays for the air conditioner, appliances, and pests."],
    "l12": ["A home-insurance quote before you get the keys.", "Whether tenant insurance is required by law in Saint-Martin, as it is in mainland France, is to be confirmed. The lease will often require it anyway.", "Ask the insurer about hurricane and 'catastrophe naturelle' cover. The detail of that regime is to be confirmed."],
    "l13": ["Every earlier lease line ticked, or a written reason you are waiting.", "The deposit amount you will actually pay."],
    "l9": ["The move-in inspection (état des lieux), with photos and video, on the day you get the keys.", "Both of you present if you can."],
    "l10": ["The lease clause that says when the deposit comes back, and to which account."],
    "hs05": ["The lease, proof of address, and ID, which EDF will ask for. The exact list is to be confirmed when you call.", "The start date, matched to your move-in day.", "Phone and hours are in the contact card. Hours are to be confirmed."],
    "hs06": ["The same ID and proof of address.", "SAUR's phone is in the contact card. EEASM's public desk is Wednesday and Thursday, 8:00 a.m. to 2:00 p.m., on eeasm.org."],
    "hs07": ["Do this only if you later want to buy. Renting does not require it.", "A notaire or adviser. Purchase costs and property tax in Saint-Martin differ from mainland France. The amounts are to be confirmed. This app is not tax or legal advice."],
    "v1": ["A rental booking with pickup at SXM.", "The contract must allow driving on the French side. Ask before you pay.", "Your licence and passport. The deductible, and what your credit card covers."],
    "v2": ["The date you become a resident. The one-year clock starts then, not on the day you land for a short visit.", "The Collectivité page, updated Sept 9, 2026, says a non-EU licence must be exchanged and is recognized for one year after you take up normal residence. That sentence also says 'en métropole'. Ask the Service des titres if the same one-year clock applies in Saint-Martin. To be confirmed."],
    "vh01": ["The US state that issued each licence.", "The exchange simulator the Collectivité page points to. The state list changes. Florida was on Scout's May 2026 note. Check the list again. To be confirmed.", "If your state is not on the list, you sit the French exam. The page says you do not have to do the 20-hour minimum if you already hold a valid foreign licence."],
    "uw03": ["The expiry date of each current licence.", "Renew with the state before you leave if it expires soon. The fee is that state's fee. To be confirmed on the state site."],
    "vh02": ["A driving record from the state that issued the licence.", "Ask the Collectivité if they also want that record apostilled. To be confirmed."],
    "vh03": ["A sworn translation of the licence and of the driving record, if the Service des titres asks for one.", "The translator quote."],
    "vh04": ["Proof of address under 3 months old. The checklist says the Collectivité wants that for a licence. Less than 6 months is the visiteur-card rule. They are different.", "Passport, visa or residence paper, photos, the licence, the driving record, and translations.", "The PDF list on the Collectivité site opened on Oct 29, 2026. Use that list, not a homemade one.", "Fee: the approved checklist says €150 each. That amount was not on the exchange page checked Oct 29, 2026. To be confirmed at the desk."],
    "v12": ["The folder from the step above.", "An appointment, or a confirmed walk-in time. Call 0590 87 61 91 first. Hours are to be confirmed.", "You hand in the foreign licence. Ask whether a Saint-Martin licence is valid for driving in mainland France and the rest of the EU. To be confirmed."],
    "v4": ["Three to five prices for similar used cars on the island, written in notes.", "No seller's papers yet. This step is only a price check."],
    "vh05": ["A written decision: buy on the island, or ship a car.", "Shipping a car raises customs questions. Ask the customs office (Douane) in Saint-Martin. The national individuals page opened Oct 29, 2026. It is not a Saint-Martin vehicle page. The local rule is to be confirmed.", "Scout's older note: buying locally is usually simpler."],
    "v9": ["A mechanic who will inspect the car before you pay.", "The seller's permission for that visit.", "A mechanic's name from a person you trust, not only from the seller."],
    "vh06": ["The seller's ID, the registration (carte grise), and proof the car is not financed.", "A bill of sale. The exact set is on the Collectivité registration page. Read it before you pay."],
    "v5": ["Insurance that starts before you drive away.", "At least third-party liability (responsabilité civile), which service-public F2628 describes as compulsory.", "Ask the insurer if the policy covers the Dutch side of the island. To be confirmed.", "Your US auto policy does not cover living here."],
    "v11": ["ID, proof of address, insurance attestation, and the seller's papers.", "The fee on the Collectivité registration page, checked Oct 29, 2026: for a car, €36 per fiscal horsepower if the vehicle is under 10 years old, and €18 per fiscal horsepower if it is over 10 years old. Motorcycles have lower figures on that same page. Plates are separate.", "The Service des titres address and phone are in the contact card."],
    "vh07": ["The question for the Service des titres: is a contrôle technique required in Saint-Martin, and how often? To be confirmed.", "No fee is listed until they answer."],
    "ml01": ["A choice: family address, or a virtual US mailbox.", "Ask your bank and your state whether they will accept a virtual mailbox. To be confirmed with them."],
    "ml02": ["A USPS change of address, filed in person if the page says in person.", "The USPS forwarding page opened Oct 29, 2026.", "Plan as if USPS will not forward to a foreign address, until the page or the clerk says it will. To be confirmed."],
    "ml03": ["The question for the landlord: does La Poste deliver to this street, or do we need a box?", "To be confirmed for your actual address."],
    "ml04": ["Only if the landlord says mail does not come to the door.", "A La Poste box (BP). Price and availability are to be confirmed at the office. The La Poste page blocked an automatic check.", "The Marigot post office address in Scout is to be confirmed. See the contact card."],
    "ml05": ["What counts as proof of address. service-public F14807 opened Oct 29, 2026.", "A bill in your name. The Justif'Adresse online check does not work in a collectivity like Saint-Martin, per the approved checklist. Bring the paper.", "Licence files want proof under 3 months old. The visiteur card page says under 6 months. Match the office you are visiting."],
    "ml06": ["The three latest bills that show your name and the Saint-Martin address, in one folder."],
    "ml07": ["Each adult's state, for the FVAP state guide. The FVAP pages opened Oct 29, 2026.", "This is free."],
    "ml08": ["The backup ballot instructions on the FVAP citizen-voter page.", "A calendar reminder before each federal election."],
    "ph1": ["Your T-Mobile plan name (or the other US carrier).", "The international-roaming page opened Oct 29, 2026. Whether your own plan includes Saint-Martin, and for how many months, is to be confirmed in your account. Roaming is for travel. Carriers can limit a long stay."],
    "pn01": ["A choice for each US number: keep the US line, move it to Google Voice, or another option.", "Ask each bank if they will send sign-in codes to that option. To be confirmed with the bank. Do not cancel a number until the bank says yes."],
    "pn02": ["Only if you chose Google Voice.", "Do the port before you leave the US. Google's help page opened Oct 29, 2026.", "Google's porting fee is on that page. Read the current amount there."],
    "ph5": ["Each phone's settings page that shows lock status and eSIM.", "A Samsung Galaxy Z Fold3 and a Galaxy Tab S10 Lite can be checked in Settings. Write 'unlocked' or 'locked' in notes. If a phone is locked to a carrier, ask that carrier to unlock it before you fly."],
    "ph2": ["Roaming switched on for each line, in the carrier app, before the flight.", "A test text."],
    "ph4": ["Backup codes for email, stored offline.", "A second way in, not only one phone."],
    "ph6": ["Prices, eSIM support, and the ID each carrier wants (passport, proof of address). All four of those are to be confirmed in the shop.", "French-side carriers named in the checklist: Orange Caraïbe, Digicel, Free Caraïbe, Dauphin Telecom. Their sites opened on Oct 29, 2026. Digicel's address redirected to its web store.", "No plan price is copied here, because the live price was not on a page we could quote."],
    "pn03": ["Passport.", "The shop's price, written down before you pay.", "Keep the US number working on the other line."],
    "ph8": ["WhatsApp on each phone, using the number you want people to call.", "Wi-Fi calling switched on if your US carrier allows it. That rule is in your carrier's account. To be confirmed there."],
    "ph9": ["Your plan's rule for the Dutch side. Near the border the phone can jump to a Dutch network and bill roaming.", "A test while you are out, on the French side, to see which network name shows."],
    "in2": ["The exact street address of the home.", "Orange's fibre page for Saint-Martin opened Oct 29, 2026. Eligibility still has to be checked for that address. Price and install time are to be confirmed with Orange."],
    "in3": ["The same street address.", "Dauphin Telecom's site opened Oct 29, 2026. Ask them about fibre at that address, in writing."],
    "in4": ["Starlink's site opened Oct 29, 2026. The live price for French Saint-Martin is on that site. A third-party figure in Scout (about €70 a month and a €349 kit) is to be confirmed there. Do not use the third-party number as the price.", "Written permission from the landlord before you mount a dish."],
    "pn04": ["Your new local number.", "A list of banks, SSA, and insurers to update. Do this after the SIM works."],
    "uw01": ["A talk with your tax preparer.", "The decision affects voting, state tax, and the driving-licence clock. Your state's rule is to be confirmed.", "Write the decision in notes in plain words, such as 'we are leaving Florida for tax purposes on this date'."],
    "uw02": ["The end date of the current health plan.", "The start date of the new plan, which must be earlier. No gap."],
    "uw04": ["A talk with an estate lawyer at home, and later a notaire in Saint-Martin.", "How French inheritance rules apply to foreign residents of Saint-Martin is to be confirmed with the notaire. This app is not legal advice.", "Beneficiary names on accounts. Do not type account numbers here."],
    "uw05": ["A power of attorney and a health-care proxy, signed before you leave.", "A lawyer in your home state. Doing this from abroad is harder. No fee is listed. The lawyer will quote."],
    "m30_6": ["A list of subscriptions, utilities, gym, storage and insurance, with an end date for each.", "Tick them in the notes box as you cancel them."],
    "mv_home": ["The lease end already stored in this app: Nov 19, 2026, unless you change it on the Home screen.", "A final-inspection appointment.", "Utility shutoff, and a forwarding address for the deposit."],
    "pt01": ["Only if you have a pet. The example plan has none. If you have no pet, mark this done and write 'no pets'.", "The Shipping and Pets section of this app, and DAAF Guadeloupe, which covers Saint-Martin.", "Current rules for your animal are to be confirmed with DAAF. The Dutch-side USDA page is a different rule. Do not use it for the French side."],
    "sc03": ["Both phones.", "The four numbers in the contact card, saved offline."],
    "sc01": ["A STEP account for each adult. The STEP page blocked an automatic check. Open it in Chrome.", "Your Saint-Martin address, once you have it. You can start the account before that.", "This is free."],
    "sc02": ["The embassy card below, saved in both phones.", "The State Department French West Indies page. It blocked an automatic check. Open it in Chrome and look for the local consular agent."],
    "sc04": ["Passport scans already in cloud storage, from the civil-records steps.", "The embassy's lost-passport instructions, saved offline. Read them on the embassy site. The exact click-path was not re-copied here."],
}

TIPS = {
    "h8": ["Open the two links below. On France-Visas, the document list for your file is the one to follow. The automatic check could not open that site."],
    "hc01": ["On service-public F34308, read the part for people who are not working in France. The page opened on Oct 29, 2026."],
    "hc11": ["Medicare does not pay for routine care outside the United States. Read the Medicare travel page before you decide. Do not drop Part B on a guess about the penalty."],
    "b16": ["The older banking checklist still tells you to mail SSA-1199-FR to Paris. Treat that as archived advice. Use this step instead, and wait for SSA to name the office."],
    "mv_ssa": ["US Embassy Bridgetown has posted visits about Social Security benefits. The page opened on Oct 29, 2026. Read it for the next visit. It does not by itself prove which office owns French Saint-Martin."],
    "ld28": ["If Nov 19, 2026 is still the leaving date, count backward. A centre will not take the file more than 3 months early, and you want the appointment at least a month before you go. That window may already be too tight. Decide with Michael whether to move later, or to arrive as visitors and apply from the US afterward."],
    "ld31": ["Open ANEF, create the account, and follow the validation screens. Pay the tax the screen shows. If the site rejects a Saint-Martin address, stop and call the préfecture. Do not invent a mainland address."],
    "ld35": ["On F302, the fee is paid with timbres fiscaux (tax stamps), bought online or at a tobacco shop. The page says the proof of payment is asked when the card is handed over."],
    "l5": ["Service-public pages on mainland leases are linked so you can see the mainland rule. They are not proof that Saint-Martin uses the same rule."],
    "v2": ["You do not use the mainland ANTS website for this exchange. The Collectivité does it, and the licence it issues is a Saint-Martin licence."],
    "v11": ["Plate numbers in Saint-Martin belong to the person, not the car, according to the approved checklist. Confirm that with the desk when you register."],
    "vh05": ["Open douane.gouv.fr/particuliers and look for moving your household goods. The old vehicle-import links in earlier drafts were dead and were not used."],
    "in4": ["On starlink.com, set the service address to the French side, postal code 97150, and read the price on that screen."],
    "ph6": ["Compare in a shop, not only online. Take your passport. Ask them to write the monthly price and the commitment length on the receipt."],
    "ml02": ["Go to a US post office with ID. The forwarding page is the official start. If the clerk says foreign forwarding is not available, use the virtual mailbox from the step above."],
    "sc01": ["On the STEP site, create the account, add Saint-Martin, and turn on email alerts. The page blocked an automatic check, so the button names may have changed. Follow what you see."],
    "it05": ["The 5-year rule page, updated April 29, 2026, says Saint-Martin's tax is separate from mainland France and from the overseas departments. It also says foreign nationals living in Saint-Martin are part of the residence question. There is no separate filing deadline for the residence question. Settle it before you file a return."],
    "tx6": ["Two calendars, not one. US return: automatic extension to June 15 if you are abroad, from the IRS page. Saint-Martin return: May 31, from the Collectivité page updated April 29, 2026."],
    "hs06": ["Call SAUR on 0590 87 97 03 for a new water account. The EEASM desk is only Wednesday and Thursday."],
    "b15": ["On the IEDOM droit-au-compte page, download the form. You need a written bank refusal. The Guadeloupe agency is the one that covers you. There is also a once-a-month desk in Marigot. See the contact card."],
    "pt01": ["Open the Shipping and Pets section in the menu. Use the DAAF Guadeloupe link there. Ignore the USDA page titled St. Maarten / St. Martin for French-side entry. That page is the Dutch-side rule."],
    "uw04": ["No notaire phone was verified for this step. Ask the ADIL or the préfecture receptionist for the current notaire list, then confirm on the notaire's own door or site. A national directory page was not used, because it did not open in the earlier check."],
}


def when_label(rule):
    if not rule:
        return ""
    bits = []
    if rule.get("needsVisa") is True:
        bits.append("Only if you need a visa (you do, as US citizens, unless that changes)")
    if rule.get("hasPets") is True:
        bits.append("Only if you have a pet")
    if "citizenship" in rule:
        bits.append("For citizens of: " + ", ".join(rule["citizenship"]))
    if rule.get("married") is True:
        bits.append("Only if you are married")
    if rule.get("worksRemotely") is True:
        bits.append("Only if one of you works remotely")
    if rule.get("plansToDrive") is True:
        bits.append("Only if you will drive")
    if rule.get("plansToOwnCar") is True:
        bits.append("Only if you will own a car")
    if rule.get("licenceIssuedOutsideEU") is True:
        bits.append("Only if the licence was issued outside the EU")
    if rule.get("plansToBuy") is True:
        bits.append("Only if you plan to buy a home")
    if rule.get("usMedicare") is True:
        bits.append("Only if you are on Medicare")
    extra = [k for k in rule.keys() if k not in (
        "needsVisa", "hasPets", "citizenship", "married", "worksRemotely",
        "plansToDrive", "plansToOwnCar", "licenceIssuedOutsideEU", "plansToBuy",
        "usMedicare", "note")]
    for k in extra:
        bits.append(k + ": " + json.dumps(rule[k], ensure_ascii=False))
    return ". ".join(bits)


def have_ready(item):
    rows = [
        "Time to allow: %s." % item.get("estTime") or "not listed",
        "Who: %s." % (item.get("appliesTo") or "household"),
    ]
    if item.get("dependsOn"):
        rows.append("Do these first: " + ", ".join(item["dependsOn"]) + ".")
    if item.get("cost"):
        rows.append("Fee named in the checklist: %s." % item["cost"])
    else:
        rows.append("No fee is listed for this step. If an office asks you to pay, ask what it is for and write the amount in your notes.")
    rows.extend(DOCS.get(item["id"], []))
    if item["id"] not in DOCS:
        rows.append("Nothing further is listed. Follow the steps and write dates in your notes.")
    return rows


def tips_for(item, cat):
    rows = []
    if item.get("saintMartinDiff"):
        rows.append(item["saintMartinDiff"])
    rows.extend(TIPS.get(item["id"], []))
    if item.get("verify"):
        rows.append("Still to confirm: " + item["verify"])
    if item.get("sourceNote"):
        rows.append(item["sourceNote"])
    checked = item.get("lastVerified")
    src = item.get("source") or "No source named"
    if checked:
        rows.append("Source: %s. Last checked %s. Look again every %s." % (src, checked, item.get("reviewEvery") or "6 months"))
    else:
        rows.append("Source: %s. No check date on this step, because it depends on a person or a company rather than a public page. Look again every %s." % (src, item.get("reviewEvery") or "6 months"))
    return rows


def main():
    states = load_link_states()
    raw = json.loads(SRC.read_text())
    verified = flagged = 0
    missing_docs = []
    categories = []
    for cat in raw["categories"]:
        items = []
        for it in cat["items"]:
            if it["id"] not in DOCS:
                missing_docs.append(it["id"])
            links = []
            for link in it.get("links") or []:
                st = states.get(link["url"])
                if not st:
                    st = {"state": "flagged", "detail": "This address was not in the Oct 29, 2026 recheck. Open it in Chrome. Not treated as verified."}
                if st["state"] == "verified":
                    verified += 1
                else:
                    flagged += 1
                links.append({
                    "label": link["label"],
                    "url": link["url"],
                    "state": st["state"],
                    "detail": st["detail"],
                })
            cids = []
            for cid in CAT_CONTACTS.get(cat["id"], []) + ITEM_CONTACTS.get(it["id"], []):
                if cid not in cids:
                    cids.append(cid)
            items.append({
                "id": it["id"],
                "title": it["title"],
                "phase": it.get("phase"),
                "steps": it.get("steps") or [],
                "links": links,
                "haveReady": have_ready(it),
                "tips": tips_for(it, cat),
                "contactIds": cids,
                "appliesTo": it.get("appliesTo"),
                "appliesWhenLabel": when_label(it.get("appliesWhen")),
                "order": it.get("order"),
                "estTime": it.get("estTime"),
                "storeKey": cat.get("appTrackerKey") or ("sxm-guide-" + cat["id"]),
                "mapsTo": it.get("mapsTo") or [],
                "source": it.get("source"),
                "lastVerified": it.get("lastVerified"),
            })
        categories.append({
            "id": cat["id"],
            "title": cat["title"],
            "intro": cat.get("intro"),
            "differs": cat.get("saintMartinDiffers"),
            "appSection": cat.get("appSection"),
            "items": items,
        })
    if missing_docs:
        raise SystemExit("missing docs for " + ", ".join(missing_docs))
    # every contact id used must exist
    used = set()
    for c in categories:
        for it in c["items"]:
            used.update(it["contactIds"])
    missing_c = used - set(CONTACTS)
    if missing_c:
        raise SystemExit("missing contacts " + ", ".join(sorted(missing_c)))
    data = {
        "checked": "2026-10-29",
        "approved": raw.get("generated"),
        "region": raw.get("region"),
        "verifiedLinks": verified,
        "flaggedLinks": flagged,
        "itemCount": sum(len(c["items"]) for c in categories),
        "disclaimer": "These steps are a planning aid from public pages and from Scout's own notes. They are not legal, tax, immigration, or medical advice. Offices change hours and fees. Each step shows when its source was last checked.",
        "timeline": "The Home screen still has your current lease ending November 19, 2026. A long-stay visa is applied for before you leave the United States. The visa centre takes files no more than 3 months ahead, and the checklist says to book at least a month before you go. If that November date still holds, you may have to arrive as visitors (90 days in any 180) and go back to the United States to apply. Decide this before you book flights. This is a planning question, not a legal opinion.",
        "questions": [
            "Is November 19, 2026 still the move date, or do you wait until the visa is in the passport?",
            "Will either of you work remotely after the move? That changes the visa and the tax steps.",
            "Is either of you on Medicare now, or turning 65 soon? A yes or no is enough.",
            "Will you own a car in Saint-Martin, or rent for a long time?",
            "Which state issued each driving licence, and in which states were you born and married? State names only.",
            "Should Social Security be paid to a US account or a euro account? Ask SSA before you close the US account.",
        ],
        "contacts": CONTACTS,
        "categories": categories,
        "legacyPrefix": {
            "hi": "sxm-hi-docs2",
            "legal": "sxm-legal-docs2",
            "bank": "sxm-bank-docs2",
            "lease": "sxm-lease-docs2",
            "veh": "sxm-veh-docs2",
            "tax": "sxm-tax-docs2",
            "phone": "sxm-phone-docs2",
            "inet": "sxm-inet-docs2",
            "move": "sxm-move-docs2",
            "cl": "sxm-cl2",
            "ship": "sxm-ship-docs2",
            "cost": "sxm-cost-docs2",
            "work": "sxm-work-docs2",
        },
    }
    OUT.write_text("window.SXMGuide = " + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + ";\n", encoding="utf-8")
    print("items", data["itemCount"], "verified", verified, "flagged", flagged, "bytes", OUT.stat().st_size)


if __name__ == "__main__":
    main()
