# ZDI-16-502: Bitdefender Antivirus Plus avc3 Kernel Driver Untrusted Pointer Dereference Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-502
- **ZDI-CAN:** ZDI-CAN-3829
- **Date:** 2016-09-01
- **CVE:** N/A
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Bitdefender
- **Affected Products:** Antivirus Plus
- **Credit:** bear13oy of CloverSec Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-502/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Bitdefender Antivirus Plus. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the processing of IOCTL 0x002222f4 by the avc3 kernel driver. The issue lies in the failure to validate a user-supplied value prior to dereferencing it as a pointer. An attacker can leverage this vulnerability to execute arbitrary code under the context of kernel.

## Additional Details

Bitdefender has issued an update to correct this vulnerability. More details can be found at: http://www.bitdefender.com/site/view/bug-bounty-hall-of-fame.html

## Disclosure Timeline

- 2016-06-21 - Vulnerability reported to vendor
- 2016-09-01 - Coordinated public release of advisory
