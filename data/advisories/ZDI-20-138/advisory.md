# ZDI-20-138: Oracle VirtualBox xHCI Time-Of-Check Time-Of-Use Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-138
- **ZDI-CAN:** ZDI-CAN-9794
- **Date:** 2020-01-15
- **CVE:** CVE-2020-2702
- **CVSS:** 7.5
- **CVSS Vector:** AV:L/AC:H/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** Lucas Leong of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-138/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Oracle VirtualBox. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the xHCI component. The issue results from the lack of proper locking when performing operations on an object. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpujan2020.html

## Disclosure Timeline

- 2019-11-22 - Vulnerability reported to vendor
- 2020-01-15 - Coordinated public release of advisory
