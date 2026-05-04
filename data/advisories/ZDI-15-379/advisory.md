# ZDI-15-379: Microsoft Internet Explorer Registry Link Elevation of Privilege Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-379
- **ZDI-CAN:** ZDI-CAN-2758
- **Date:** 2015-08-11
- **CVE:** CVE-2015-2429
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Ashutosh Mehra (https://twitter.com/ashutoshmehra)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-379/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of registry links. An attacker running code in a low-integrity Internet Explorer process can set a registry link that will be followed by the medium-integrity broker process, which will then reduce the security of the target registry key in such a way that it can be modified by low-integrity Internet Explorer processes. These registry keys can be used to execute medium-integrity processes from low-integrity Internet Explorer processes.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS15-090

## Disclosure Timeline

- 2015-02-12 - Vulnerability reported to vendor
- 2015-08-11 - Coordinated public release of advisory
