# ZDI-16-487: AVG Internet Security avgtdix.sys Kernel Driver Untrusted Pointer Dereference Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-487
- **ZDI-CAN:** ZDI-CAN-3761
- **Date:** 2016-08-19
- **CVE:** N/A
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** AVG
- **Affected Products:** Internet Security
- **Credit:** bee13oy of CloverSec Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-487/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of AVG Internet Security. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within processing of the 0x83002120 IOCTL by the AvgTdix device driver. The issue lies in the failure to properly validate a user-supplied value prior to dereferencing it as a pointer. An attacker can leverage this vulnerability to execute arbitrary code under the context of kernel.

## Additional Details

Patched in fixed in AVG Internet Security version 16.101.0.7752, which was released on August 4, 2016.

## Disclosure Timeline

- 2016-05-31 - Vulnerability reported to vendor
- 2016-08-19 - Coordinated public release of advisory
