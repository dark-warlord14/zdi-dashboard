# ZDI-19-668: (Pwn2Own) Oracle VirtualBox vusbUrbSubmitCtrl Use-After-Free Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-668
- **ZDI-CAN:** ZDI-CAN-8572
- **Date:** 2019-07-22
- **CVE:** CVE-2019-2859
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** Anthony LAOU HINE TSUEI (@anarcheuz)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-668/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on affected installations of Oracle VirtualBox. An attacker must first obtain the ability to execute low-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the vusbUrbSubmitCtrl method. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/technetwork/security-advisory/cpujul2019-5072835.html

## Disclosure Timeline

- 2019-06-26 - Vulnerability reported to vendor
- 2019-07-22 - Coordinated public release of advisory
