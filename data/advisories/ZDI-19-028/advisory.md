# ZDI-19-028: Schneider Electric IIoT Monitor RuleMgmt addRule XML External Entity Processing Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-028
- **ZDI-CAN:** ZDI-CAN-7133
- **Date:** 2019-01-14
- **CVE:** CVE-2018-7837
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Schneider Electric
- **Affected Products:** IIot Monitor
- **Credit:** rgod of 9sg Security Team - rgod@9sgsec.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-028/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Schneider Electric IIoT Monitor. Authentication is not required to exploit this vulnerability. The specific flaw exists in the addRule method of the RuleMgmt servlet. Due to the improper restriction of XML External Entity (XXE) references, a specially crafted document specifying a URI causes the XML parser to access the URI and embed the contents back into the XML document for further processing. An attacker can leverage this in conjunction with other vulnerabilities to bypass authentication on the system.

## Additional Details

Schneider Electric has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-19-008-02

## Disclosure Timeline

- 2018-08-14 - Vulnerability reported to vendor
- 2019-01-14 - Coordinated public release of advisory
