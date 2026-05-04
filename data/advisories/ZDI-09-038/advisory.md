# ZDI-09-038: Microsoft Internet Explorer Event Handler Memory Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-038
- **ZDI-CAN:** ZDI-CAN-428
- **Date:** 2009-06-10
- **CVE:** CVE-2009-1530
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** ling&wushi of team509
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-038/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists when repeatedly calling event handlers after adding nodes of an HTML document. When a specially crafted webpage is repeatedly rendered, memory is improperly reused after it has been freed. Due to the controllable nature of the web browser, this vulnerability can be exploited to remotely compromise a system running under the security context of the currently logged in user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/MS09-019.mspx

## Disclosure Timeline

- 2009-01-26 - Vulnerability reported to vendor
- 2009-06-10 - Coordinated public release of advisory
