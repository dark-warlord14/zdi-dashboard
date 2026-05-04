# ZDI-21-428: Parallels Desktop Toolgate Stack-based Buffer Overflow Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-428
- **ZDI-CAN:** ZDI-CAN-12220
- **Date:** 2021-04-21
- **CVE:** CVE-2021-31420
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Parallels
- **Affected Products:** Desktop
- **Credit:** Ezrak1e
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-428/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Parallels Desktop. An attacker must first obtain the ability to execute low-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the Toolgate component. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the hypervisor.

## Additional Details

Parallels has issued an update to correct this vulnerability. More details can be found at: https://kb.parallels.com/en/125013

## Disclosure Timeline

- 2020-12-16 - Vulnerability reported to vendor
- 2021-04-21 - Coordinated public release of advisory
- 2021-06-29 - Advisory Updated
