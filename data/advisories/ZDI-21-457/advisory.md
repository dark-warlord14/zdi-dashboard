# ZDI-21-457: Oracle VirtualBox VGA Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-457
- **ZDI-CAN:** ZDI-CAN-12621
- **Date:** 2021-04-22
- **CVE:** CVE-2021-2291
- **CVSS:** 5.5
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** JungHyun Kim(@jidoc01) of VirtualBoBs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-457/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Oracle VirtualBox. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the VGA component. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges and execute arbitrary code in the context of the kernel.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpuapr2021.html

## Disclosure Timeline

- 2021-01-08 - Vulnerability reported to vendor
- 2021-04-22 - Coordinated public release of advisory
