# ZDI-20-904: Oracle VirtualBox BusLogicSCSI Uninitialized Memory Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-904
- **ZDI-CAN:** ZDI-CAN-11273
- **Date:** 2020-07-20
- **CVE:** CVE-2020-14704
- **CVSS:** 6.0
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:N/A:N
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** Lucas Leong (@_wmliang_) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-904/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Oracle VirtualBox. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the BusLogicSCSI component. The issue results from the lack of proper initialization of memory prior to accessing it. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpujul2020.html

## Disclosure Timeline

- 2020-06-17 - Vulnerability reported to vendor
- 2020-07-20 - Coordinated public release of advisory
