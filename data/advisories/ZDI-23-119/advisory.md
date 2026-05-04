# ZDI-23-119: Oracle VirtualBox Teleporter Improper Error Handling Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-119
- **ZDI-CAN:** ZDI-CAN-18864
- **Date:** 2023-02-09
- **CVE:** CVE-2023-21886
- **CVSS:** 8.1
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** Exist(@exist91240480)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-119/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Oracle VirtualBox. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Teleporter service. The issue results from the lack of proper error handling when validating teleporter credentials. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpujan2023.html

## Disclosure Timeline

- 2022-11-01 - Vulnerability reported to vendor
- 2023-02-09 - Coordinated public release of advisory
