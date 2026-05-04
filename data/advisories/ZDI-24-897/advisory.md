# ZDI-24-897: Trend Micro Apex One modOSCE SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-897
- **ZDI-CAN:** ZDI-CAN-22968
- **Date:** 2024-07-05
- **CVE:** CVE-2024-39753
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Apex One
- **Credit:** N1k0la (@webdxg)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-897/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Trend Micro Apex One. Authentication is required to exploit this vulnerability. The specific flaw exists within the client management functionality. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of IUSR.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/dcx/s/solution/000298063

## Disclosure Timeline

- 2024-02-13 - Vulnerability reported to vendor
- 2024-07-05 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
