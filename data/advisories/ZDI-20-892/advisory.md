# ZDI-20-892: Oracle VirtualBox LsiLogicSCSI Time-Of-Check Time-Of-Use Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-892
- **ZDI-CAN:** ZDI-CAN-10978
- **Date:** 2020-07-20
- **CVE:** CVE-2020-14650
- **CVSS:** 5.3
- **CVSS Vector:** AV:L/AC:H/PR:H/UI:N/S:C/C:H/I:N/A:N
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** Lucas Leong (@_wmliang_) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-892/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Oracle VirtualBox. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the lsilogicFinishAddressReply function. The issue results from the lack of proper locking when performing operations on an object. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpujul2020.html

## Disclosure Timeline

- 2020-04-28 - Vulnerability reported to vendor
- 2020-07-20 - Coordinated public release of advisory
