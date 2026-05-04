# ZDI-25-107: (Pwn2Own) HP LaserJet Pro MFP 3301fdw PostScript File Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-107
- **ZDI-CAN:** ZDI-CAN-25594
- **Date:** 2025-03-03
- **CVE:** CVE-2025-26506
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** HP
- **Affected Products:** LaserJet Pro MFP 3301fdw
- **Credit:** Felipe Jacob Custodio Romero, Neodyme AG
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-107/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of HP LaserJet Pro MFP 3301fdw printers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the parsing of PostScript data. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

HP has issued an update to correct this vulnerability. More details can be found at: https://support.hp.com/us-en/document/ish_11953771-11953793-16/hpsbpi04007

## Disclosure Timeline

- 2024-12-02 - Vulnerability reported to vendor
- 2025-03-03 - Coordinated public release of advisory
- 2025-03-03 - Advisory Updated
