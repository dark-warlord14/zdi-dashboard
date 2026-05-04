# ZDI-23-687: Canonical ksmbd-tools LSARPC Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-687
- **ZDI-CAN:** ZDI-CAN-17770
- **Date:** 2023-05-17
- **CVE:** N/A
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Canonical
- **Affected Products:** ksmbd-tools
- **Credit:** Arnaud Gatignol, Quentin Minster, Florent Saudel, Guillaume Teissier (@thalium_team)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-687/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Canonical ksmbd-tools. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of the LSARPC_OPNUM_LOOKUP_SID2 opcode. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Fixed in 3.4.8 https://github.com/cifsd-team/ksmbd-tools/releases/tag/3.4.8

## Disclosure Timeline

- 2022-07-26 - Vulnerability reported to vendor
- 2023-05-17 - Coordinated public release of advisory
