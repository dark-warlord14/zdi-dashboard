# ZDI-20-893: Oracle VirtualBox PCnet Time-Of-Check Time-Of-Use Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-893
- **ZDI-CAN:** ZDI-CAN-10898
- **Date:** 2020-07-20
- **CVE:** CVE-2020-14677
- **CVSS:** 7.5
- **CVSS Vector:** AV:L/AC:H/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** Reno Robert of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-893/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Oracle VirtualBox. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the handling of Transmit Message Descriptors in the implementation of PCnet virtual network interfaces. The issue results from the lack of proper locking when performing operations on an object. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpujul2020.html

## Disclosure Timeline

- 2020-05-06 - Vulnerability reported to vendor
- 2020-07-20 - Coordinated public release of advisory
- 2021-03-02 - Advisory Updated
