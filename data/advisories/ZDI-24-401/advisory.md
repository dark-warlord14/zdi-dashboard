# ZDI-24-401: Progress Software Telerik Reporting ObjectReader Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-401
- **ZDI-CAN:** ZDI-CAN-23001
- **Date:** 2024-04-25
- **CVE:** CVE-2024-1801
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Progress Software
- **Affected Products:** Telerik Reporting
- **Credit:** 07842c0e165d4d2d8733dd4eab48b3ed0f7afe38
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-401/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Progress Software Telerik Reporting. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the ObjectReader class. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

Progress Software has issued an update to correct this vulnerability. More details can be found at: https://docs.telerik.com/reporting/knowledge-base/deserialization-vulnerability-cve-2024-1801-cve-2024-1856

## Disclosure Timeline

- 2024-02-14 - Vulnerability reported to vendor
- 2024-04-25 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
