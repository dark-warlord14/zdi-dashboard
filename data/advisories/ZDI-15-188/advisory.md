# ZDI-15-188: Microsoft Windows NtUserRealInternalGetMessage Stack Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-188
- **ZDI-CAN:** ZDI-CAN-2751
- **Date:** 2015-05-12
- **CVE:** CVE-2015-1680
- **CVSS:** 4.9
- **CVSS Vector:** AV:L/AC:L/Au:N/C:C/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** WanderingGlitch - HP Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-188/
## Vulnerability Details

This vulnerability allows local attackers to leak sensitive information on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the NtUserRealInternalGetMessage function. The issue lies in the failure to sanitize a buffer before returning its contents resulting in the leak of a kernel address. An attacker can leverage this together with another vulnerability to achieve code execution at SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS15-051

## Disclosure Timeline

- 2015-03-05 - Vulnerability reported to vendor
- 2015-05-12 - Coordinated public release of advisory
