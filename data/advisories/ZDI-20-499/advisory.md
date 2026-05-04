# ZDI-20-499: Oracle VirtualBox xHCI Integer Overflow Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-499
- **ZDI-CAN:** ZDI-CAN-10022
- **Date:** 2020-04-16
- **CVE:** CVE-2020-2742
- **CVSS:** 8.2
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** Reno Robert of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-499/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Oracle VirtualBox. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the xHCI component. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before allocating a buffer. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpuapr2020.html

## Disclosure Timeline

- 2020-01-10 - Vulnerability reported to vendor
- 2020-04-16 - Coordinated public release of advisory
- 2021-03-02 - Advisory Updated
