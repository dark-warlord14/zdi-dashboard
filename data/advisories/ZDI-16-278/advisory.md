# ZDI-16-278: (Pwn2Own) Microsoft Windows xxxEndDeferWindowPosEx Window Use-After-Free Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-278
- **ZDI-CAN:** ZDI-CAN-3609
- **Date:** 2016-05-10
- **CVE:** CVE-2016-0196
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** 360Vulcan
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-278/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of Window objects. The issue lies in the failure to increment a reference counter prior to calling userland code. An attacker can leverage this vulnerability to escalate privileges and execute code within the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/ms16-062.aspx

## Disclosure Timeline

- 2016-03-12 - Vulnerability reported to vendor
- 2016-05-10 - Coordinated public release of advisory
