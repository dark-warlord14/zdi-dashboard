# ZDI-16-670: Avira Free Antivirus ssmdrv Kernel Driver Memory Corruption Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-670
- **ZDI-CAN:** ZDI-CAN-3809
- **Date:** 2016-12-15
- **CVE:** N/A
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Avira
- **Affected Products:** Free Antivirus
- **Credit:** bee13oy of CloverSec Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-670/
## Vulnerability Details

This vulnerability allows attackers to escalate privileges on vulnerable installations of Avira Free Antivirus. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the processing of IOCTL 0x00220010 by the ssmdrv driver. The issue lies in failure to properly validate user-supplied data which can result in a memory corruption condition within the kernel. An attacker can leverage this vulnerability to execute arbitrary code under the context of the kernel.

## Additional Details

The reported vulnerability should be fixed now with the version 15.0.22.54.

## Disclosure Timeline

- 2016-06-14 - Vulnerability reported to vendor
- 2016-12-15 - Coordinated public release of advisory
