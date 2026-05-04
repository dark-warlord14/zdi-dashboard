# ZDI-20-887: Oracle VirtualBox virtio-net Uninitialized Memory Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-887
- **ZDI-CAN:** ZDI-CAN-10795
- **Date:** 2020-07-20
- **CVE:** CVE-2020-14629
- **CVSS:** 6.0
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:N/A:N
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** Reno Robert of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-887/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Oracle VirtualBox. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the virtio-net component. The issue results from the lack of proper validation of a user-supplied value prior to dereferencing it as a pointer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpujul2020.html

## Disclosure Timeline

- 2020-04-14 - Vulnerability reported to vendor
- 2020-07-20 - Coordinated public release of advisory
- 2021-03-02 - Advisory Updated
