# ZDI-16-503: Bitdefender Antivirus Plus bdfwfpf Integer Overflow Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-503
- **ZDI-CAN:** ZDI-CAN-3749
- **Date:** 2016-09-01
- **CVE:** N/A
- **CVSS:** 6.6
- **CVSS Vector:** AV:L/AC:M/Au:S/C:C/I:C/A:C
- **Affected Vendors:** Bitdefender
- **Affected Products:** Antivirus Plus
- **Credit:** bear13oy of CloverSec Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-503/
## Vulnerability Details

This vulnerability allows local attackers to escalate their privileges on vulnerable installations of Bitdefender Antivirus Plus. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within processing of the 0x8000e038 IOCTL by the bdfwfpf device driver. A crafted buffer sent to the DeviceIoControl API can cause the corruption of pool memory in the kernel because of an integer overflow in the calculation of length for a memcpy command. An attacker can leverage this vulnerability execute arbitrary code in the context of SYSTEM.

## Additional Details

Bitdefender has issued an update to correct this vulnerability. More details can be found at: http://www.bitdefender.com/site/view/bug-bounty-hall-of-fame.html

## Disclosure Timeline

- 2016-05-12 - Vulnerability reported to vendor
- 2016-09-01 - Coordinated public release of advisory
