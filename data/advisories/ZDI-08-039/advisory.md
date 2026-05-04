# ZDI-08-039: Microsoft Internet Explorer DOM Object substringData() Heap Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-039
- **ZDI-CAN:** ZDI-CAN-269
- **Date:** 2008-06-10
- **CVE:** CVE-2008-1442
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Anonymous Peter Vreugdenhil Sebastian Apelt (webmaster@buzzworld.org)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-039/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of various Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists in the substringData() method when called on a DOM object that has been manipulated in a special way. The attack results in an exploitable heap buffer allowing for code execution under the context of the current user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/Bulletin/MS08-031.mspx

## Disclosure Timeline

- 2008-02-07 - Vulnerability reported to vendor
- 2008-06-10 - Coordinated public release of advisory
