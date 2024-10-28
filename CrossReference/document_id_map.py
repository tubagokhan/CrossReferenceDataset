#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 15:09:25 2024

@author: tuba.gokhan
"""

# document_id_map.py

# Document ID to Document Name mapping
DOCUMENT_ID_MAP = {
    1: [
        "AML_VER09.211223",
        "AML",
        "Anti-Money Laundering and Sanctions Rules and Guidance",
        "Anti-Money Laundering and Sanctions Rules and Guidance (AML)"
    ],
    2: [
        "CIB_VER04.030220",
        "CIB",
        "Captive Insurance Business Rules (CIB)",
        "Captive Insurance Business Rules"
    ],
    3: [
        "COBS_VER15.150823",
        "COBS",
        "COBs",
        "Conduct of Business Rulebook"
    ],
    4: [
        "FEES_VER16.181223",
        "Fees Rules (FEES)",
        "FEES"
    ],
    5: [
        "FP_VER01.110319",
        "Fund Passporting Rules (FP)",
        "FP"
    ],
    6: [
        "FUNDS_VER08.040723",
        "FUNDS",
        "Fund Rules (FUNDS)"
    ],
    7: [
        "GEN_VER08.181223",
        "GEN",
        "General Rulebook (GEN)",
        "General Rulebook"
    ],
    8: [
        "GLO_VER19.181223",
        "GLO",
        "GLOSSARY (GLO)"
    ],
    9: [
        "IFR_VER07.181223",
        "IFR",
        "Islamic Finance Rules (IFR)",
        "Islamic Finance Rules"
    ],
    10: [
        "MIR_VER07.181223",
        "MIR",
        "Market Infrastructure Rulebook (MIR)",
        "Market Infrastructure Rulebook"
    ],
    11: [
        "MKT_VER08.181223",
        "MKT",
        "Market Rules (MKT)",
        "Market Rules"
    ],
    12: [
        "PIN_VER05.181223",
        "PIN",
        "Prudential – Insurance Business (PIN)",
        "Prudential – Insurance Business"
    ],
    13: [
        "PRU_VER13.181223",
        "PRU",
        "Prudential – Investment, Insurance Intermediation and Banking Rules (PRU)",
        "Prudential – Investment, Insurance Intermediation and Banking Rules"
    ],
    14: [
        "BRR Regulations (December 2018)",
        "BRR Regulations",
        "BRR",
        "BANK RECOVERY AND RESOLUTION REGULATIONS 2018",
        "BANK RECOVERY AND RESOLUTION REGULATIONS"
    ],
    15: [
        "CRS Regulations 2017 (Consolidated_October 2023)",
        "CRS",
        "COMMON REPORTING STANDARD REGULATIONS 2017",
        "COMMON REPORTING STANDARD REGULATIONS"
    ],
    16: [
        "Foreign Tax Account Compliance Regulations 2022",
        "FOREIGN ACCOUNT TAX COMPLIANCE REGULATIONS"
    ],
    17: [
        "FSMR (Consolidated_December 2023)",
        "FSMR",
        "FINANCIAL SERVICES AND MARKETS REGULATIONS 2015"
    ],
    18: [
        "Guidance – Regulatory Framework for Fund Managers of Venture Capital Funds (VER03.181223)",
        "Guidance – Regulatory Framework for Fund Managers of Venture Capital Funds"
    ],
    19: [
        "Guidance - Virtual Asset Activities in ADGM (VER05.181223)",
        "Guidance – Regulation of Virtual Asset Activities in ADGM"
    ],
    20: [
        "ADGM_Guidance_-_Application_of_English_Laws",
        "Guidance - English Law in ADGM"
    ],
    21: [
        "API - Guidance Note_Final 14 October 2019 Eng",
        "Guidance – Application Programming Interfaces (APIs) in ADGM"
    ],
    22: [
        "CMC_VER03.270922",
        "CMC",
        "Code of Market Conduct (CMC)",
        "Code of Market Conduct"
    ],
    23: [
        "CONF_VER03.18042019",
        "CONF",
        "FSRA Confidentiality Policy"
    ],
    24: [
        "Draft Guidance - FSRA Guiding Principles for Virtual Assets Regulation and Supervision (IA)",
        "Guiding Principles for the Financial Services Regulatory Authority’s Approach to Virtual Asset Regulation and Supervision"
    ],
    25: [
        "Environmental Social and Governance Disclosures Guidance_VER01.040723",
        "ESG Disclosures Guidance",
        "Environmental Social Governance Guidance"
    ],
    26: [
        "FinTech RegLab Guidance_VER01.31082016",
        "FinTech Regulatory Laboratory Guidance"
    ],
    27: [
        "GPM_VER03.120623",
        "GPM",
        "Guidance & Policies Manual (GPM)",
        "Guidance & Policies Manual"
    ],
    28: [
        "Guidance - Continuous Disclosure_VER01.280922",
        "Guidance – Continuous Disclosure"
    ],
    29: [
        "Guidance - Digital Securities Offerings and Virtual Assets under the Financial Services and Markets Regulations_240220",
        "Guidance –Regulation of Digital Security Offerings and Virtual Assets under the Financial Services and Markets Regulations"
    ],
    30: [
        "Guidance - Disclosure Requirements for Mining Reporting Entities_VER01.280922",
        "Guidance – Disclosure Requirements for Mining Reporting Entities"
    ],
    31: [
        "Guidance - Disclosure Requirements for Petroleum Reporting Entities_VER01.280922",
        "Guidance – Disclosure Requirements for Petroleum Reporting Entities"
    ],
    32: [
        "Guidance - Private Credit Funds_VER01.040523",
        "Supplementary Guidance – Private Credit Funds"
    ],
    33: [
        "Guidance Regulation of Digital Securities Activities in ADGM_240224",
        "Guidance – Regulation of Digital Securities Activities in ADGM",
        "Guidance – Regulation of Digital Securities Activities"
    ],
    34: [
        "Guidance - Regulation of Spot Commodities Activities in ADGM (VER02.181223)",
        "Guidance – Regulation of Spot Commodity Activities in ADGM"
    ],
    35: [
        "Guidance_Regulatory Framework for PFP and Multilateral Trading Facilities dealing with Private Capital Markets (VER02.181223)",
        "Guidance – Regulatory Framework for Private Financing Platforms and Multilateral Trading Facilities dealing with Private Capital Markets"
    ],
    36: [
        "SFWG_Guidance on Principles for the Effective Management of Climate-related Financial Risks",
        "Guidance - Principles for the Effective Management of Climate-related Financial Risks"
    ],
    37: [
        "Supplementary Guidance Authorisation of Digital Investment Management (Robo-advisory) Activities",
        "Supplementary Guidance – Authorisation of Digital Investment Management (“Robo-advisory”) Activities"
    ],
    38: [
        "Supplementary Guidance OTCLPs (VER02.181223)",
        "Supplementary Guidance – Regulatory Framework for Authorised Persons dealing in OTC Leveraged Products for Retail Clients"
    ],
    39: [
        "Sustainable Finance Supplementary Guidance_VER01.040723",
        "Supplementary Guidance – Sustainable Finance Regulatory Framework"
    ],
    40: [
        "UAE_CRS_Guidance_Notes_17 June 2020 (002)",
        "Guidance Notes for the Common Reporting Standard (CRS) United Arab Emirates",
        "CRS"
    ]
}
