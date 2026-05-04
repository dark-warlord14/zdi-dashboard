# ZDI-24-403: Progress Software Telerik Report Server ObjectReader Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-403
- **ZDI-CAN:** ZDI-CAN-23903
- **Date:** 2024-04-25
- **CVE:** CVE-2024-1800
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Progress Software
- **Affected Products:** Telerik Report Server
- **Credit:** 07842c0e165d4d2d8733dd4eab48b3ed0f7afe38
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-403/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Progress Software Telerik Report Server. Authentication is required to exploit this vulnerability. The specific flaw exists within the ObjectReader class. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Progress Software has issued an update to correct this vulnerability. More details can be found at: https://docs.telerik.com/report-server/knowledge-base/deserialization-vulnerability-cve-2024-1800

## Disclosure Timeline

- 2024-04-25 - Vulnerability reported to vendor
- 2024-04-25 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
