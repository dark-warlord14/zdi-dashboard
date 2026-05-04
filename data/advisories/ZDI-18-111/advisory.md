# ZDI-18-111: Trend Micro Control Manager AdHocQuery_Processor External Entity Processing Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-111
- **ZDI-CAN:** ZDI-CAN-5232
- **Date:** 2018-01-10
- **CVE:** CVE-2018-3600
- **CVSS:** 4.0
- **CVSS Vector:** AV:N/AC:L/Au:S/C:P/I:N/A:N
- **Affected Vendors:** Trend Micro
- **Affected Products:** Control Manager
- **Credit:** Steven Seeley (mr_me) of Offensive Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-111/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Trend Micro Control Manager. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within processing of AdHocQuery_Processor. Due to the improper restriction of XML External Entity (XXE) reference, a specially crafted URI causes the XML parser to access the contents of this URI and embed these contents back into the XML document for further processing. An attacker can leverage this vulnerability to disclose sensitive information under the context of the Network Service account.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/1119158

## Disclosure Timeline

- 2017-10-05 - Vulnerability reported to vendor
- 2018-01-10 - Coordinated public release of advisory
