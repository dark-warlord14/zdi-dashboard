# ZDI-16-483: AVG Internet Security avgidsdriverx.sys Untrusted Pointer Dereference Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-483
- **ZDI-CAN:** ZDI-CAN-3732
- **Date:** 2016-08-18
- **CVE:** N/A
- **CVSS:** 6.8
- **CVSS Vector:** AV:L/AC:L/Au:S/C:C/I:C/A:C
- **Affected Vendors:** AVG
- **Affected Products:** Internet Security
- **Credit:** bee13oy of CloverSec Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-483/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of AVG Internet Security. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within processing of the 0x53606148 IOCTL in the avgidsdriverx driver. A crafted buffer sent to this IOCTL causes memory corruption in the kernel. An attacker could leverage this vulnerability to execute arbitrary code in the context of SYSTEM.

## Additional Details

AVG has issued an update to correct this vulnerability. More details can be found at: http://files-download.avg.com/inst/mp/AVG_Internet_Security_695.exe Patched in AVG Internet Security version 16.81.7639, which was released on May 26, 2016.

## Disclosure Timeline

- 2016-05-12 - Vulnerability reported to vendor
- 2016-08-18 - Coordinated public release of advisory
