# ZDI-21-1231: Oracle E-Business Suite Content-Length Memory Exhaustion Denial-Of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1231
- **ZDI-CAN:** ZDI-CAN-14228
- **Date:** 2021-10-21
- **CVE:** CVE-2021-35611
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:L
- **Affected Vendors:** Oracle
- **Affected Products:** E-Business Suite
- **Credit:** John Simpson of Trend Micro Security Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1231/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Oracle E-Business Suite. Authentication is required to exploit this vulnerability. The specific flaw exists within the processing of the Content-Length HTTP header. The issue results from the lack of proper validation of user-supplied data, which can result in a memory exhaustion condition. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpuoct2021.html

## Disclosure Timeline

- 2021-06-30 - Vulnerability reported to vendor
- 2021-10-21 - Coordinated public release of advisory
