# ZDI-17-501: Trend Micro Control Manager BasePageSessionExpire External Entity Processing Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-501
- **ZDI-CAN:** ZDI-CAN-4706
- **Date:** 2017-07-31
- **CVE:** CVE-2017-11390
- **CVSS:** 4.0
- **CVSS Vector:** AV:N/AC:L/Au:S/C:P/I:N/A:N
- **Affected Vendors:** Trend Micro
- **Affected Products:** Control Manager
- **Credit:** @vftable
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-501/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Trend Micro Control Manager. Authentication is required to exploit this vulnerability. The specific flaw exists within BasePageSessionExpire.cs. Due to the improper restriction of XML External Entity (XXE) reference, a specially crafted URI causes the XML parser to access the contents of this URI and embed these contents back into the XML document for further processing. An attacker can leverage this vulnerability to disclose sensitive information under the context of the current process.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/1117722

## Disclosure Timeline

- 2017-04-13 - Vulnerability reported to vendor
- 2017-07-31 - Coordinated public release of advisory
