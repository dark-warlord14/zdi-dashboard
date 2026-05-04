# ZDI-20-508: Oracle VirtualBox SLiRP Networking Out-Of-Bounds Access Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-508
- **ZDI-CAN:** ZDI-CAN-10416
- **Date:** 2020-04-16
- **CVE:** CVE-2020-2929
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** Vishnu Dev TJ
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-508/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Oracle VirtualBox. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of NAT. The issue results from the lack of proper validation of user-supplied data, which can result in a memory access past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpuapr2020.html

## Disclosure Timeline

- 2020-03-18 - Vulnerability reported to vendor
- 2020-04-16 - Coordinated public release of advisory
