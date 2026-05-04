# ZDI-21-459: Oracle VirtualBox LsiLogicSCSI Race Condition Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-459
- **ZDI-CAN:** ZDI-CAN-12854
- **Date:** 2021-04-22
- **CVE:** CVE-2021-2296
- **CVSS:** 5.3
- **CVSS Vector:** AV:L/AC:H/PR:H/UI:N/S:C/C:H/I:N/A:N
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** Lucas Leong (@_wmliang_) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-459/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Oracle VirtualBox. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the implementation of the LsiLogic virtual device. The issue results from the lack of proper locking when performing operations on an object. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges and execute arbitrary code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpuapr2021.html

## Disclosure Timeline

- 2021-01-15 - Vulnerability reported to vendor
- 2021-04-22 - Coordinated public release of advisory
