# ZDI-21-425: Parallels Desktop Toolgate Directory Traversal Arbitrary File Deletion Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-425
- **ZDI-CAN:** ZDI-CAN-12129
- **Date:** 2021-04-21
- **CVE:** CVE-2021-31421
- **CVSS:** 3.2
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:N/I:L/A:N
- **Affected Vendors:** Parallels
- **Affected Products:** Desktop
- **Credit:** Ezrak1e
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-425/
## Vulnerability Details

This vulnerability allows local attackers to delete arbitrary files on affected installations of Parallels Desktop. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the Toolgate component. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to delete arbitrary files in the context of the hypervisor.

## Additional Details

Parallels has issued an update to correct this vulnerability. More details can be found at: https://kb.parallels.com/en/125013

## Disclosure Timeline

- 2020-12-23 - Vulnerability reported to vendor
- 2021-04-21 - Coordinated public release of advisory
- 2021-06-29 - Advisory Updated
