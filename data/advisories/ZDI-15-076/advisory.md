# ZDI-15-076: Microsoft Windows Text Services Out-Of-Bounds Memory Access Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-076
- **ZDI-CAN:** ZDI-CAN-2571
- **Date:** 2015-03-10
- **CVE:** CVE-2015-0081
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Garage4Hackers
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-076/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The vulnerability relates to how Windows Text Services processes certain objects. By opening a malformed document, an attacker can force MSCFT.dll to access memory outside the bounds of an array. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS15-020

## Disclosure Timeline

- 2014-10-31 - Vulnerability reported to vendor
- 2015-03-10 - Coordinated public release of advisory
