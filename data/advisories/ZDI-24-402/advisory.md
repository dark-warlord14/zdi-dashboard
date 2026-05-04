# ZDI-24-402: Progress Software Telerik Reporting ObjectReader Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-402
- **ZDI-CAN:** ZDI-CAN-23902
- **Date:** 2024-04-25
- **CVE:** CVE-2024-1856
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Progress Software
- **Affected Products:** Telerik Reporting
- **Credit:** 07842c0e165d4d2d8733dd4eab48b3ed0f7afe38
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-402/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Progress Software Telerik Reporting. Authentication is required to exploit this vulnerability. The specific flaw exists within the ObjectReader class. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Progress Software has issued an update to correct this vulnerability. More details can be found at: https://docs.telerik.com/reporting/knowledge-base/deserialization-vulnerability-cve-2024-1801-cve-2024-1856

## Disclosure Timeline

- 2024-04-25 - Vulnerability reported to vendor
- 2024-04-25 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
