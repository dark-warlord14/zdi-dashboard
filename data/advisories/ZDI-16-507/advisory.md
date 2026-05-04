# ZDI-16-507: Microsoft Windows NtGdiQueryFonts Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-507
- **ZDI-CAN:** ZDI-CAN-3756
- **Date:** 2016-09-16
- **CVE:** CVE-2016-3354
- **CVSS:** 4.9
- **CVSS Vector:** AV:L/AC:L/Au:N/C:C/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** WanderingGlitch - Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-507/
## Vulnerability Details

This vulnerability allows local attackers to leak sensitive information on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the NtGdiQueryFonts function. The issue lies in the failure to sanitize a buffer before returning its contents resulting in the leak of a kernel address. An attacker can leverage this vulnerability to leak sensitive information in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS16-106

## Disclosure Timeline

- 2016-05-05 - Vulnerability reported to vendor
- 2016-09-16 - Coordinated public release of advisory
