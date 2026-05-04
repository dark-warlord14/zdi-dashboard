# ZDI-17-635: Microsoft Windows CLFS Driver Buffer Overflow Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-635
- **ZDI-CAN:** ZDI-CAN-4773
- **Date:** 2017-08-08
- **CVE:** CVE-2017-8624
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Jaanus Kp Clarified Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-635/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Common Log File System (CLFS) driver. A crafted call to this driver can trigger an overflow of a buffer. An attacker can leverage this vulnerability to escalate privilege to the level of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2017-8624

## Disclosure Timeline

- 2017-05-05 - Vulnerability reported to vendor
- 2017-08-08 - Coordinated public release of advisory
