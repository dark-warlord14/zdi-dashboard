# ZDI-15-079: Microsoft Windows NtUserfnINSTRINGNULL Information Leak Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-079
- **ZDI-CAN:** ZDI-CAN-2590
- **Date:** 2015-03-10
- **CVE:** CVE-2015-0077
- **CVSS:** 2.1
- **CVSS Vector:** AV:L/AC:L/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** WanderingGlitch of HP's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-079/
## Vulnerability Details

This vulnerability allows local attackers to leak sensitive information on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of NtUserfnINSTRINGNULL function. The issue lies in the failure to sanitize a buffer before calling a userland function resulting in the leak of a kernel address. An attacker can leverage this in concert with another vulnerability to achieve code execution at SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS15-023

## Disclosure Timeline

- 2014-12-04 - Vulnerability reported to vendor
- 2015-03-10 - Coordinated public release of advisory
