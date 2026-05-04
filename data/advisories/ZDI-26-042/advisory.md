# ZDI-26-042: (0Day) Upsonic Cloudpickle Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-042
- **ZDI-CAN:** ZDI-CAN-26845
- **Date:** 2026-01-09
- **CVE:** CVE-2026-0773
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Upsonic
- **Affected Products:** Upsonic
- **Credit:** Alessio Dalla Piazza (Equixly)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-042/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Upsonic. Authentication is not required to exploit this vulnerability. The specific flaw exists within the add_tool endpoint, which listens on TCP port 7541 by default. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

05/08/25 – ZDI requested the vendor’s PSIRT contacts 06/19/25 – the vendor provided their contacts 06/19/25 - ZDI submitted the report to the vendor 10/10/25 – ZDI asked for updates 11/06/25 – ZDI asked for updates 12/09/25 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product

## Disclosure Timeline

- 2025-06-19 - Vulnerability reported to vendor
- 2026-01-09 - Coordinated public release of advisory
- 2026-01-09 - Advisory Updated
