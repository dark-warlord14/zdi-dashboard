# ZDI-16-196: Microsoft Windows CreateWindowStation Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-196
- **ZDI-CAN:** ZDI-CAN-3589
- **Date:** 2016-03-10
- **CVE:** CVE-2016-0095
- **CVSS:** 7.2
- **CVSS Vector:** AV:L/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** bee13oy of CloverSec Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-196/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of CreateWindowStation. The issue lies in the failure to check for NULL before dereferencing a pointer. An attacker can leverage this vulnerability to elevate privileges and execute code within the context of the kernel.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/MS16-034

## Disclosure Timeline

- 2016-03-03 - Vulnerability reported to vendor
- 2016-03-10 - Coordinated public release of advisory
