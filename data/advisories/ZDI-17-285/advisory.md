# ZDI-17-285: Microsoft Windows Font Object Buffer Overflow Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-285
- **ZDI-CAN:** ZDI-CAN-4337
- **Date:** 2017-04-11
- **CVE:** CVE-2017-0155
- **CVSS:** 7.2
- **CVSS Vector:** AV:L/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** bear13oy of CloverSec Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-285/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the processing of font data in win32k.sys. By making API calls with crafted parameters, code can trigger an overflow of a buffer. An attacker can leverage this vulnerability to escalate privilege to SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2017-0155

## Disclosure Timeline

- 2016-12-12 - Vulnerability reported to vendor
- 2017-04-11 - Coordinated public release of advisory
