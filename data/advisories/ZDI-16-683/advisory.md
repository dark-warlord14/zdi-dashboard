# ZDI-16-683: Check Point ZoneAlarm Extreme Security vsdatant Kernel Driver Untrusted Pointer Dereference Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-683
- **ZDI-CAN:** ZDI-CAN-3760
- **Date:** 2017-06-02
- **CVE:** N/A
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Check Point
- **Affected Products:** ZoneAlarm Extreme Security
- **Credit:** bee13oy of CloverSec Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-683/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Check Point ZoneAlarm Extreme Security. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the processing of IOCTL 0x8400001f by the vsdatant kernel driver. The issue lies in the failure to validate a user-supplied value prior to dereferencing it as a pointer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code under the context of kernel.

## Additional Details

The fixed version was online starting early September (ver 15.0.123.17051).

## Disclosure Timeline

- 2016-07-28 - Vulnerability reported to vendor
- 2017-06-02 - Coordinated public release of advisory
