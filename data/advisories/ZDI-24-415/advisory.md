# ZDI-24-415: (Pwn2Own) Oracle VirtualBox E1000 Uninitialized Memory Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-415
- **ZDI-CAN:** ZDI-CAN-23775
- **Date:** 2024-04-26
- **CVE:** CVE-2024-21113
- **CVSS:** 6.0
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:N/A:N
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** dungdm(@_piers2) of Viettel Cyber Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-415/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Oracle VirtualBox. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the implementation of the E1000 virtual device. The issue results from the lack of proper initialization of memory prior to accessing it. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpuapr2024.html

## Disclosure Timeline

- 2024-03-28 - Vulnerability reported to vendor
- 2024-04-26 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
