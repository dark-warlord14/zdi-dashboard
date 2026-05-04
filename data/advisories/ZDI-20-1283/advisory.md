# ZDI-20-1283: Oracle E-Business Suite ozfVendorLov SQL Injection Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1283
- **ZDI-CAN:** ZDI-CAN-11687
- **Date:** 2020-10-22
- **CVE:** CVE-2020-14876
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Oracle
- **Affected Products:** E-Business Suite
- **Credit:** Tuan Anh Nguyen of Viettel Cyber Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1283/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on affected installations of Oracle E-Business Suite. Authentication is not required to exploit this vulnerability. The specific flaw exists within ozfVendorLov.jsp. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpuoct2020.html

## Disclosure Timeline

- 2020-10-14 - Vulnerability reported to vendor
- 2020-10-22 - Coordinated public release of advisory
