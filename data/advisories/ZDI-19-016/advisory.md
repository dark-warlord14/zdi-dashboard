# ZDI-19-016: Microsoft Visual Studio wpa Protocol XML External Entity Processing Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-016
- **ZDI-CAN:** ZDI-CAN-7251
- **Date:** 2019-01-10
- **CVE:** N/A
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Visual Studio
- **Credit:** rgod of 9sg Security Team - rgod@9sgsec.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-016/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Microsoft Visual Studio. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handler for the Windows Performance Analyzer (wpa) protocol. Due to the improper restriction of XML External Entity (XXE) references, a specially crafted document specifying a URI causes the XML parser to access the URI and embed the contents back into the XML document for further processing. An attacker can leverage this vulnerability to disclose information in the context of the current user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://developer.microsoft.com/en-US/windows/downloads/windows-10-sdk

## Disclosure Timeline

- 2018-09-20 - Vulnerability reported to vendor
- 2019-01-10 - Coordinated public release of advisory
