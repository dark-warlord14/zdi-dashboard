# ZDI-17-168: Microsoft Windows DrawIconEx Buffer Overflow Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-168
- **ZDI-CAN:** ZDI-CAN-4052
- **Date:** 2017-03-21
- **CVE:** CVE-2017-0047
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** bear13oy of CloverSec Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-168/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the code in the Windows kernel that renders icons. By supplying certain parameter values in a call to DrawIconEx, an attacker can trigger an overflow of a buffer. An attacker can leverage this vulnerability to escalate privilege to SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/MS17-0113

## Disclosure Timeline

- 2016-10-06 - Vulnerability reported to vendor
- 2017-03-21 - Coordinated public release of advisory
