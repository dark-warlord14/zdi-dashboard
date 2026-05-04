# ZDI-21-455: Oracle VirtualBox NAT Integer Underflow Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-455
- **ZDI-CAN:** ZDI-CAN-13473
- **Date:** 2021-04-22
- **CVE:** CVE-2021-2145
- **CVSS:** 7.5
- **CVSS Vector:** AV:L/AC:H/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** Max Van Amerongen (maxpl0it)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-455/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Oracle VirtualBox. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the implementation of NAT. The issue results from the lack of proper validation of user-supplied data, which can result in an integer underflow before writing to memory. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpuapr2021.html

## Disclosure Timeline

- 2021-04-14 - Vulnerability reported to vendor
- 2021-04-22 - Coordinated public release of advisory
