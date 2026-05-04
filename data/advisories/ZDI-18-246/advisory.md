# ZDI-18-246: Microsoft Windows Palette Object Race Condition Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-246
- **ZDI-CAN:** ZDI-CAN-5446
- **Date:** 2018-03-19
- **CVE:** CVE-2018-0815
- **CVSS:** 7.2
- **CVSS Vector:** AV:L/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Marcin Wiazowski
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-246/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the win32k.sys driver. When handling a palette object, a race condition exists due to the failure to lock an object in memory between operations. An attacker can leverage this vulnerability to escalate privileges to the level of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-0815

## Disclosure Timeline

- 2017-12-01 - Vulnerability reported to vendor
- 2018-03-19 - Coordinated public release of advisory
- 2018-03-19 - Advisory Updated
