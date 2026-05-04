# ZDI-22-1443: Oracle Access Management CustomReadServlet Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1443
- **ZDI-CAN:** ZDI-CAN-17705
- **Date:** 2022-10-21
- **CVE:** CVE-2022-39412
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Oracle
- **Affected Products:** Access Management
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1443/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Oracle Access Management. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the ContextValue parameter provided to the CustomReadServlet endpoint. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpuoct2022.html

## Disclosure Timeline

- 2022-08-03 - Vulnerability reported to vendor
- 2022-10-21 - Coordinated public release of advisory
