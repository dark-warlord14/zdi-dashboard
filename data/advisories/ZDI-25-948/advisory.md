# ZDI-25-948: Jaspersoft Jasper Reports JRLoader Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-948
- **ZDI-CAN:** ZDI-CAN-27130
- **Date:** 2025-10-07
- **CVE:** CVE-2025-10492
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Jaspersoft
- **Affected Products:** Jasper Reports
- **Credit:** Swagat
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-948/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Jaspersoft Jasper Reports. Interaction with this library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the JRLoader class. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Jaspersoft has issued an update to correct this vulnerability. More details can be found at: https://community.jaspersoft.com/advisories/jaspersoft-security-advisory-september-16-2025-jaspersoft-library-cve-2025-10492-r6/

## Disclosure Timeline

- 2025-06-10 - Vulnerability reported to vendor
- 2025-10-07 - Coordinated public release of advisory
- 2025-10-07 - Advisory Updated
