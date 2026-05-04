# ZDI-16-592: Microsoft Windows win32k.sys Bitmap Null Pointer Dereference Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-592
- **ZDI-CAN:** ZDI-CAN-3924
- **Date:** 2016-11-08
- **CVE:** CVE-2016-7215
- **CVSS:** 7.2
- **CVSS Vector:** AV:L/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** bee13oy of CloverSec Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-592/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of bitmap objects. By performing a certain sequence of calls to win32k.sys, an attacker can cause the kernel to make use of a null pointer. An attacker can leverage this vulnerability to escalate privilege to SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS16-135

## Disclosure Timeline

- 2016-07-29 - Vulnerability reported to vendor
- 2016-11-08 - Coordinated public release of advisory
