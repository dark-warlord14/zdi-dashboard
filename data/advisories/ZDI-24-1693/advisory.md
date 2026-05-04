# ZDI-24-1693: Dell Avamar Web Restore Login Action SQL Injection Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1693
- **ZDI-CAN:** ZDI-CAN-25066
- **Date:** 2024-12-16
- **CVE:** CVE-2024-47484
- **CVSS:** 8.2
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:L
- **Affected Vendors:** Dell
- **Affected Products:** Avamar
- **Credit:** Kentaro Kawane of GMO Cybersecurity by Ierae
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1693/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Dell Avamar. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of the clientPath parameter provided to the webRestoreLogin.action endpoint. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

Dell has issued an update to correct this vulnerability. More details can be found at: https://www.dell.com/support/kbdoc/en-us/000258636/dsa-2024-489-security-update-for-dell-avamar-and-dell-avamar-virtual-edition-security-update-for-multiple-vulnerabilities

## Disclosure Timeline

- 2024-09-12 - Vulnerability reported to vendor
- 2024-12-16 - Coordinated public release of advisory
- 2024-12-16 - Advisory Updated
