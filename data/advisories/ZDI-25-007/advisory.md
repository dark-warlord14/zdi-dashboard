# ZDI-25-007: Trend Micro Apex One widget getWidgetPoolManager Local File Inclusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-007
- **ZDI-CAN:** ZDI-CAN-23401
- **Date:** 2025-01-08
- **CVE:** CVE-2024-52047
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Apex One
- **Credit:** N1k0la (@webdxg)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-007/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Trend Micro Apex One. Authentication is required to exploit this vulnerability. The specific flaw exists within the getWidgetPoolManager function. The issue results from the lack of proper validation of user-supplied data prior to passing it to a PHP include function. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of IUSR.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/en-US/solution/KA-0016669

## Disclosure Timeline

- 2024-02-15 - Vulnerability reported to vendor
- 2025-01-08 - Coordinated public release of advisory
- 2025-01-08 - Advisory Updated
