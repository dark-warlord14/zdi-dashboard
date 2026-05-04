# ZDI-16-681: Avast Free Antivirus aswSnx Kernel Driver Untrusted Pointer Dereference Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-681
- **ZDI-CAN:** ZDI-CAN-3712
- **Date:** 2017-05-11
- **CVE:** N/A
- **CVSS:** 7.2
- **CVSS Vector:** AV:L/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Avast
- **Affected Products:** Free Antivirus
- **Credit:** bee13oy of CloverSec Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-681/
## Vulnerability Details

This vulnerability allows attackers to elevate their privileges on vulnerable installations of Avast Free Antivirus. Authentication is not required to exploit this vulnerability. The specific flaw exists within processing of the 0x82ac0170 IOCTL by the aswSnx driver in the kernel. An address passed into the kernel through a DeviceIoControl call is trusted and used without validation. An attacker could leverage this vulnerability to execute arbitrary code in the context of the kernel.

## Additional Details

Fixed in Avast v12.1, released 21 June 2016.

## Disclosure Timeline

- 2016-04-29 - Vulnerability reported to vendor
- 2017-05-11 - Coordinated public release of advisory
