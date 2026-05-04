# ZDI-24-822: (Pwn2Own) HP Color LaserJet Pro MFP 4301fdw CFF Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-822
- **ZDI-CAN:** ZDI-CAN-22377
- **Date:** 2024-06-21
- **CVE:** CVE-2024-0794
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** HP
- **Affected Products:** Color LaserJet Pro MFP 4301fdw
- **Credit:** @vcslab
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-822/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of HP Color LaserJet Pro MFP 4301fdw printers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the parsing of embedded fonts. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

HP has issued an update to correct this vulnerability. More details can be found at: https://support.hp.com/us-en/document/ish_10174031-10174074-16/hpsbpi03917

## Disclosure Timeline

- 2023-11-09 - Vulnerability reported to vendor
- 2024-06-21 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
