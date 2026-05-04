# ZDI-21-209: Parallels Desktop Toolgate Out-Of-Bounds Write Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-209
- **ZDI-CAN:** ZDI-CAN-11926
- **Date:** 2021-02-24
- **CVE:** CVE-2021-27242
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Parallels
- **Affected Products:** Desktop
- **Credit:** Ezrak1e
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-209/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Parallels Desktop. An attacker must first obtain the ability to execute low-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the Toolgate component. The issue results from the lack of proper validation of user-supplied data, which can result in a memory corruption condition. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the hypervisor.

## Additional Details

Parallels has issued an update to correct this vulnerability. More details can be found at: https://kb.parallels.com/en/125013

## Disclosure Timeline

- 2020-09-30 - Vulnerability reported to vendor
- 2021-02-24 - Coordinated public release of advisory
- 2022-09-26 - Advisory Updated
