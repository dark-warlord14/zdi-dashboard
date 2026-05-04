# ZDI-21-432: Parallels Desktop Tools Integer Overflow Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-432
- **ZDI-CAN:** ZDI-CAN-12790
- **Date:** 2021-04-21
- **CVE:** CVE-2021-31425
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Parallels
- **Affected Products:** Desktop
- **Credit:** grigoritchy
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-432/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Parallels Desktop. An attacker must first obtain the ability to execute low-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the Parallels Tools component. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before allocating a buffer. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the kernel on the target guest system.

## Additional Details

Parallels has issued an update to correct this vulnerability. More details can be found at: https://kb.parallels.com/en/125013

## Disclosure Timeline

- 2021-02-08 - Vulnerability reported to vendor
- 2021-04-21 - Coordinated public release of advisory
