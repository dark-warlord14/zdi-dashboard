# ZDI-21-451: Oracle VirtualBox VMSVGA Numeric Truncation Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-451
- **ZDI-CAN:** ZDI-CAN-13464
- **Date:** 2021-04-22
- **CVE:** CVE-2021-2266
- **CVSS:** 6.0
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:N/A:N
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** JunYoung Park (@candymate) of VirtualBoBs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-451/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Oracle VirtualBox. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the VMSVGA virtual device. The issue results from an integer truncation before reading from memory. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges and execute arbitrary code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpuapr2021.html

## Disclosure Timeline

- 2021-04-14 - Vulnerability reported to vendor
- 2021-04-22 - Coordinated public release of advisory
