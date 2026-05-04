# ZDI-20-382: Advantech WebAccess/NMS MibbrowserTrapAddAction XML External Entity Reference Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-382
- **ZDI-CAN:** ZDI-CAN-9575
- **Date:** 2020-04-08
- **CVE:** CVE-2020-10629
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess/NMS
- **Credit:** rgod of 9sg
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-382/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Advantech WebAccess/NMS. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of calls to the MibbrowserMibbrowserTrapAddAction method. Due to the improper restriction of XML External Entity (XXE) references, a specially crafted document specifying a URI causes the XML parser to access the URI and embed the contents back into the XML document for further processing. An attacker can leverage this vulnerability to disclose file contents in the context of SYSTEM.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://www.us-cert.gov/ics/advisories/icsa-20-098-01

## Disclosure Timeline

- 2019-12-11 - Vulnerability reported to vendor
- 2020-04-08 - Coordinated public release of advisory
