# ZDI-15-536: Microsoft Windows NtUserDisableProcessWindowFiltering Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-536
- **ZDI-CAN:** ZDI-CAN-2933
- **Date:** 2015-11-10
- **CVE:** CVE-2015-2367
- **CVSS:** 2.1
- **CVSS Vector:** AV:L/AC:L/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** WanderingGlitch of the HPE Security Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-536/
## Vulnerability Details

This vulnerability allows local attackers to leak sensitive information on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the NtUserDisableProcessWindowFiltering function. The issue lies in the failure to sanitize a stack variable before returning it to the user. An attacker can leverage this together with another vulnerability to achieve code execution at SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/ms15-073.aspx

## Disclosure Timeline

- 2015-05-07 - Vulnerability reported to vendor
- 2015-11-10 - Coordinated public release of advisory
