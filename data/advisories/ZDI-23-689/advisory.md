# ZDI-23-689: Canonical ksmbd-tools SAMR Null Pointer Dereference Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-689
- **ZDI-CAN:** ZDI-CAN-17821
- **Date:** 2023-05-17
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** Canonical
- **Affected Products:** ksmbd-tools
- **Credit:** Arnaud Gatignol, Quentin Minster, Florent Saudel, Guillaume Teissier (@thalium_team)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-689/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Canonical ksmbd-tools. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of the SAMR_OPNUM_QUERY_SECURITY opcode. The issue results from dereferencing a NULL pointer. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Fixed in 3.4.8 https://github.com/cifsd-team/ksmbd-tools/releases/tag/3.4.8

## Disclosure Timeline

- 2022-07-26 - Vulnerability reported to vendor
- 2023-05-17 - Coordinated public release of advisory
