# ZDI-13-235: Microsoft Windows TTF CMAP Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-235
- **ZDI-CAN:** ZDI-CAN-1882
- **Date:** 2013-10-08
- **CVE:** CVE-2013-3894
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows 7
- **Credit:** ZombiE
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-235/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of TTF fonts. The issue lies in the handling of the CMAP table. An attacker can leverage this situation to raise privileges and execute code under the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/security/bulletin/ms13-081

## Disclosure Timeline

- 2013-06-10 - Vulnerability reported to vendor
- 2013-10-08 - Coordinated public release of advisory
