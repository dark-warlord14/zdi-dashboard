# ZDI-21-483: (Pwn2Own) Oracle VirtualBox e1000 Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-483
- **ZDI-CAN:** ZDI-CAN-13545
- **Date:** 2021-04-28
- **CVE:** CVE-2021-2321
- **CVSS:** 5.3
- **CVSS Vector:** AV:L/AC:H/PR:H/UI:N/S:C/C:H/I:N/A:N
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** Billy Jheng Bing-Jhong (@st424204), Calvin Fong (@__lord_idiot) & Muhammad Alifa Ramdhan (@n0psledbyte) of STAR Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-483/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Oracle VirtualBox. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the implementation of the e1000 virtual network adapter. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges and execute arbitrary code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpuapr2021.html

## Disclosure Timeline

- 2021-04-22 - Vulnerability reported to vendor
- 2021-04-28 - Coordinated public release of advisory
