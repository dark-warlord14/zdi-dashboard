# ZDI-24-1034: Oracle VirtualBox EHCI USB Controller Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1034
- **ZDI-CAN:** ZDI-CAN-23673
- **Date:** 2024-07-30
- **CVE:** CVE-2024-21164
- **CVSS:** 2.5
- **CVSS Vector:** AV:L/AC:H/PR:H/UI:N/S:C/C:L/I:N/A:N
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** Syed Faraz Abrar (Faith) of Zellic
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1034/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Oracle VirtualBox. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the implementation of the virtual EHCI USB controller. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges and execute arbitrary code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpujul2024.html

## Disclosure Timeline

- 2024-06-12 - Vulnerability reported to vendor
- 2024-07-30 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
