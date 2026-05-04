# ZDI-18-242: Microsoft Windows Remote Assistance XML External Entity Processing Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-242
- **ZDI-CAN:** ZDI-CAN-5378
- **Date:** 2018-03-19
- **CVE:** CVE-2018-0878
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Nabeel Ahmed
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-242/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of .msrcIncident Remote Assistance invitation files. Due to the improper restriction of XML External Entity (XXE) references, a specially crafted document specifying a URI causes the XML parser to access the URI and embed the contents back into the XML document for further processing. An attacker can leverage this vulnerability to disclose information under the context of the current user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-0878

## Disclosure Timeline

- 2017-11-14 - Vulnerability reported to vendor
- 2018-03-19 - Coordinated public release of advisory
- 2018-03-19 - Advisory Updated
