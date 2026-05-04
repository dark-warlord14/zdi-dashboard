# ZDI-24-408: Oracle VirtualBox Web Service Exposure of Resource to Wrong Sphere Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-408
- **ZDI-CAN:** ZDI-CAN-23076
- **Date:** 2024-04-26
- **CVE:** CVE-2024-21109
- **CVSS:** 5.9
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-408/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Oracle VirtualBox. Authentication is not required to exploit this vulnerability. The specific flaw exists within the vboxwebsrv service. The issue results from the exposure of a resource to the wrong control sphere. An attacker can leverage this vulnerability to disclose sensitive session information, leading to further compromise.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpuapr2024.html

## Disclosure Timeline

- 2024-03-13 - Vulnerability reported to vendor
- 2024-04-26 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
