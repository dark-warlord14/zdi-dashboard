# ZDI-20-890: Oracle VirtualBox LsiLogicSCSI Out-Of-Bounds Write Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-890
- **ZDI-CAN:** ZDI-CAN-10952
- **Date:** 2020-07-20
- **CVE:** CVE-2020-14647
- **CVSS:** 7.5
- **CVSS Vector:** AV:L/AC:H/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** Lucas Leong (@_wmliang_) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-890/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Oracle VirtualBox. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the lsilogicRegisterWrite function. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpujul2020.html

## Disclosure Timeline

- 2020-04-28 - Vulnerability reported to vendor
- 2020-07-20 - Coordinated public release of advisory
