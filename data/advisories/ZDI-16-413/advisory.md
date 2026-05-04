# ZDI-16-413: Microsoft Chakra ArrayBuffer.transfer Uninitialized Buffer Information Leak Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-413
- **ZDI-CAN:** ZDI-CAN-3750
- **Date:** 2016-07-12
- **CVE:** CVE-2016-3271
- **CVSS:** 5.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Chakra
- **Credit:** WanderingGlitch of the Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-413/
## Vulnerability Details

This vulnerability allows remote attackers to leak sensitive information on vulnerable installations of Microsoft Chakra. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of ArrayBuffer.transfer. The issue lies in the failure to properly initialize a buffer prior to returning it to the user. An attacker can leverage this vulnerability to leak sensitive information within the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS16-085

## Disclosure Timeline

- 2016-05-03 - Vulnerability reported to vendor
- 2016-07-12 - Coordinated public release of advisory
