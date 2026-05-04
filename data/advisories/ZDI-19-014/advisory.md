# ZDI-19-014: Microsoft Visual Studio vscontent XML External Entity Processing Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-014
- **ZDI-CAN:** ZDI-CAN-7240
- **Date:** 2019-01-10
- **CVE:** CVE-2019-0537
- **CVSS:** 2.5
- **CVSS Vector:** AV:L/AC:H/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Visual Studio
- **Credit:** rgod of 9sg Security Team - rgod@9sgsec.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-014/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Microsoft Visual Studio. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of VSCONTENT files. Due to the improper restriction of XML External Entity (XXE) references, a specially crafted document specifying a URI causes the XML parser to access the URI and embed the contents back into the XML document for further processing. An attacker can leverage this vulnerability to disclose information in the context of the current user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0537

## Disclosure Timeline

- 2018-09-14 - Vulnerability reported to vendor
- 2019-01-10 - Coordinated public release of advisory
