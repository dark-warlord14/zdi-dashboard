# ZDI-25-216: (Pwn2Own) Synology TC500 ONVIF Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-216
- **ZDI-CAN:** ZDI-CAN-25538
- **Date:** 2025-04-09
- **CVE:** CVE-2024-11131
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Synology
- **Affected Products:** TC500
- **Credit:** Team Viettel
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-216/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Synology TC500 cameras. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of the ONVIF protocol. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Synology has issued an update to correct this vulnerability. More details can be found at: https://www.synology.com/en-us/security/advisory/Synology_SA_24_24

## Disclosure Timeline

- 2024-12-02 - Vulnerability reported to vendor
- 2025-04-09 - Coordinated public release of advisory
- 2025-04-09 - Advisory Updated
