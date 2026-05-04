# ZDI-22-941: Parallels Desktop Tools Untrusted Pointer Dereference Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-941
- **ZDI-CAN:** ZDI-CAN-16653
- **Date:** 2022-06-30
- **CVE:** CVE-2022-34890
- **CVSS:** 7.3
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:N/A:L
- **Affected Vendors:** Parallels
- **Affected Products:** Desktop
- **Credit:** Meysam Firouzi of Mbition mercedes-benz innovation lab
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-941/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Parallels Desktop. An attacker must first obtain the ability to execute low-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the Parallels Tools component. The issue results from the lack of proper validation of a user-supplied value prior to dereferencing it as a pointer. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges and execute arbitrary code in the context of the kernel.

## Additional Details

Parallels has issued an update to correct this vulnerability. More details can be found at: https://kb.parallels.com/125013

## Disclosure Timeline

- 2022-03-09 - Vulnerability reported to vendor
- 2022-06-30 - Coordinated public release of advisory
