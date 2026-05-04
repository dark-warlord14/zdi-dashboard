# ZDI-24-610: Advantech iView ConfigurationServlet SQL Injection Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-610
- **ZDI-CAN:** ZDI-CAN-17863
- **Date:** 2024-06-12
- **CVE:** CVE-2023-52335
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Advantech
- **Affected Products:** iView
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-610/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Advantech iView. Authentication is not required to exploit this vulnerability. The specific flaw exists within the ConfigurationServlet servlet, which listens on TCP port 8080 by default. When parsing the column_value element, the process does not properly validate a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://www.advantech.com/zh-tw/support/details/firmware?id=1-HIPU-183

## Disclosure Timeline

- 2022-08-19 - Vulnerability reported to vendor
- 2024-06-12 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
