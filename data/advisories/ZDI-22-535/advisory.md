# ZDI-22-535: (Pwn2Own) HP LaserJet Pro MFP M283fdw CFF Font Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-535
- **ZDI-CAN:** ZDI-CAN-15832
- **Date:** 2022-03-23
- **CVE:** CVE-2022-24292
- **CVSS:** 4.3
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N
- **Affected Vendors:** HP
- **Affected Products:** LaserJet Pro MFP M283fdw
- **Credit:** Alexander Bolshev (@dark_k3y), Timo Hirvonen (@TimoHirvonen), and Dmitry Janushkevich (@InfoSecDJ)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-535/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of HP LaserJet Pro MFP M283fdw printers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the PostScript interpreter. Crafted data in a CFF font can trigger a read past the end of an allocated data structure. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of root.

## Additional Details

https://support.hp.com/us-en/document/ish_5950417-5950443-16/hpsbpi03781

## Disclosure Timeline

- 2022-01-21 - Vulnerability reported to vendor
- 2022-03-23 - Coordinated public release of advisory
