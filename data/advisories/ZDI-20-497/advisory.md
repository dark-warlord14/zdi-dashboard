# ZDI-20-497: Oracle VirtualBox D3D9 Shader Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-497
- **ZDI-CAN:** ZDI-CAN-9960
- **Date:** 2020-04-16
- **CVE:** CVE-2020-2902
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** anhdaden of STAR Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-497/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Oracle VirtualBox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within handling of D3D9 shader objects. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpuapr2020.html

## Disclosure Timeline

- 2019-12-26 - Vulnerability reported to vendor
- 2020-04-16 - Coordinated public release of advisory
