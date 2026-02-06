# backend/hindi_normalizer.py

HINDI_MAP = {
    # Termination & validity
    "समाप्त": "terminate",
    "समाप्ति": "termination",
    "रद्द": "cancel",
    "रद्द किया": "cancelled",
    "अमान्य": "invalid",
    "वैध": "valid",

    # Penalty & liability
    "दंड": "penalty",
    "जुर्माना": "fine",
    "क्षतिपूर्ति": "indemnity",
    "उत्तरदायित्व": "liability",
    "देय": "payable",

    # Renewal & duration
    "स्वचालित": "automatic",
    "नवीकरण": "renewal",
    "अवधि": "term",
    "समयावधि": "duration",
    "तिथि": "date",
    "आरंभ": "commencement",
    "समाप्ति तिथि": "end date",

    # Rights & obligations
    "अनिवार्य": "mandatory",
    "आवश्यक": "required",
    "अधिकार": "right",
    "कर्तव्य": "obligation",
    "निषेध": "prohibited",
    "निषिद्ध": "prohibited",

    # Payment & finance
    "भुगतान": "payment",
    "राशि": "amount",
    "कुल राशि": "total amount",
    "देय राशि": "payable amount",
    "कर": "tax",
    "ब्याज": "interest",

    # IP & confidentiality
    "बौद्धिक संपदा": "intellectual property",
    "गोपनीय": "confidential",
    "गोपनीयता": "confidentiality",
    "एनडीए": "nda",

    # Arbitration & law
    "मध्यस्थता": "arbitration",
    "क्षेत्राधिकार": "jurisdiction",
    "कानून": "law",
    "शासक कानून": "governing law",

    # Parties
    "कंपनी": "company",
    "नियोक्ता": "employer",
    "कर्मचारी": "employee",
    "सेवा प्रदाता": "service provider",
    "ग्राहक": "client",
    "पक्ष": "party",
    "पक्षकार": "party",

    # Non-compete
    "प्रतिस्पर्धा": "competition",
    "गैर प्रतिस्पर्धा": "non-compete"
}

def normalize(text: str) -> str:
    """
    Replaces common Hindi legal terms with English equivalents
    to allow downstream NLP models to work uniformly.
    """
    for hindi, english in HINDI_MAP.items():
        text = text.replace(hindi, english)
    return text
