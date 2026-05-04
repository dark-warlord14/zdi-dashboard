# ZDI-14-189: (Pwn2Own) Microsoft Internet Explorer Protected Mode Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-189
- **ZDI-CAN:** ZDI-CAN-2218
- **Date:** 2014-06-11
- **CVE:** CVE-2014-2777
- **CVSS:** 7.2
- **CVSS Vector:** AV:L/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** VUPEN
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-189/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the ability to write files to arbitrary locations. The issue lies in the failure to reset state when a user cancels a file save dialog. An attacker can leverage this vulnerability to execute code as the context of the current user at medium integrity.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/ms14-035

## Disclosure Timeline

- 2014-03-13 - Vulnerability reported to vendor
- 2014-06-11 - Coordinated public release of advisory
