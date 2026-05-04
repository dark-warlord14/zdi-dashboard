# ZDI-09-039: Microsoft Internet Explorer onreadystatechange Memory Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-039
- **ZDI-CAN:** ZDI-CAN-429
- **Date:** 2009-06-10
- **CVE:** CVE-2009-1531
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer 7
- **Credit:** ling&wushi of team509
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-039/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists when repeated calls are made to getElementsByTagName() and the reordering of the elements in the document causes an object to be allocated. The use of the event "onreadystatechange" during this operation improperly frees the previously allocated resource. The combination, with repeated page rendering, leads to the exploitable memory corruption.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/MS09-019.mspx

## Disclosure Timeline

- 2009-01-26 - Vulnerability reported to vendor
- 2009-06-10 - Coordinated public release of advisory
