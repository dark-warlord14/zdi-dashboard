# ZDI-24-1691: Dell Avamar Fitness Analyzer API SQL Injection Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1691
- **ZDI-CAN:** ZDI-CAN-25067
- **Date:** 2024-12-16
- **CVE:** CVE-2024-52538
- **CVSS:** 7.1
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:L
- **Affected Vendors:** Dell
- **Affected Products:** Avamar
- **Credit:** Kentaro Kawane of GMO Cybersecurity by Ierae
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1691/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Dell Avamar. Authentication is required to exploit this vulnerability. The specific flaw exists within the processing of the start parameter provided to the report endpoint. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

Dell has issued an update to correct this vulnerability. More details can be found at: https://www.dell.com/support/kbdoc/en-us/000258636/dsa-2024-489-security-update-for-dell-avamar-and-dell-avamar-virtual-edition-security-update-for-multiple-vulnerabilities

## Disclosure Timeline

- 2024-10-03 - Vulnerability reported to vendor
- 2024-12-16 - Coordinated public release of advisory
- 2024-12-16 - Advisory Updated
