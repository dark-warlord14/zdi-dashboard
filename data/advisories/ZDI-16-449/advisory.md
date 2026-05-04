# ZDI-16-449: Microsoft Windows win32k RGNOBJ Integer Overflow Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-449
- **ZDI-CAN:** ZDI-CAN-3702
- **Date:** 2016-08-09
- **CVE:** CVE-2016-3309
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** bee13oy of CloverSec Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-449/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within RGNOBJ objects. An integer overflow vulnerability occurs when an attacker combines rectangles with special coordinates. An attacker can leverage this vulnerability to escalate privileges and execute code under the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS16-098

## Disclosure Timeline

- 2016-04-27 - Vulnerability reported to vendor
- 2016-08-09 - Coordinated public release of advisory
