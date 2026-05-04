# ZDI-18-1131: Microsoft SQL Server Management Studio xel File XML External Entity Processing Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1131
- **ZDI-CAN:** ZDI-CAN-6337
- **Date:** 2018-10-10
- **CVE:** CVE-2018-8527
- **CVSS:** 2.6
- **CVSS Vector:** AV:N/AC:H/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** SQL Server Management Studio
- **Credit:** John Page (aka hyp3rlinx) - ApparitionSec
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1131/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Microsoft SQL Server Management Studio. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of XEL files. Due to the improper restriction of XML External Entity (XXE) references, a specially crafted document specifying a URI causes the XML parser to access the URI and embed the contents back into the XML document for further processing. An attacker can leverage this vulnerability to disclose information in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-8527

## Disclosure Timeline

- 2018-06-07 - Vulnerability reported to vendor
- 2018-10-10 - Coordinated public release of advisory
- 2018-10-10 - Advisory Updated
