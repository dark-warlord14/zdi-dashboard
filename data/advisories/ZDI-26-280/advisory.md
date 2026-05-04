# ZDI-26-280: (Pwn2Own) HP DeskJet 2855e JobStatusEvent Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-280
- **ZDI-CAN:** ZDI-CAN-28366
- **Date:** 2026-04-15
- **CVE:** CVE-2026-4682
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** HP
- **Affected Products:** DeskJet 2855e
- **Credit:** Team Neodyme (@Neodyme)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-280/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of HP DeskJet 2855e printers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of SOAP requests. When handling a JobStatusEvent, the process does not properly validate the length of user-supplied data prior to copying it to a buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

HP has issued an update to correct this vulnerability. More details can be found at: https://support.hp.com/us-en/document/ish_14744451-14744475-16/hpsbpi04110

## Disclosure Timeline

- 2025-11-06 - Vulnerability reported to vendor
- 2026-04-15 - Coordinated public release of advisory
- 2026-04-15 - Advisory Updated
