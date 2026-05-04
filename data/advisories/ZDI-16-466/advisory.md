# ZDI-16-466: Joyent Smart Data Center Docker API Zone Escape Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-466
- **ZDI-CAN:** ZDI-CAN-3701
- **Date:** 2016-08-10
- **CVE:** N/A
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Joyent
- **Affected Products:** Smart Data Center
- **Credit:** Ben Murphy
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-466/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on vulnerable installations of Joyent Smart Data Center. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within a Docker remote API for this product. An attacker can create a device node that is the same as /dev/kmem, which can overwrite arbitrary kernel memory. An attacker can leverage this vulnerability to escalate privileges to escape a zone and achieve privileged execution on the Smart Data Center.

## Disclosure Timeline

- 2016-04-14 - Vulnerability reported to vendor
- 2016-08-10 - Coordinated public release of advisory
