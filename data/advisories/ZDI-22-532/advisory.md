# ZDI-22-532: (Pwn2Own) HP LaserJet Pro MFP M283fdw LLMNR Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-532
- **ZDI-CAN:** ZDI-CAN-15831
- **Date:** 2022-03-23
- **CVE:** CVE-2022-3942
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** HP
- **Affected Products:** LaserJet Pro MFP M283fdw
- **Credit:** Angelboy (@scwuaptx) from DEVCORE Research Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-532/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of HP LaserJet Pro MFP M283fdw printers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of the LLMNR protocol. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

HP has issued an update to correct this vulnerability. More details can be found at: https://support.hp.com/us-en/document/ish_5948778-5949142-16/hpsbpi03780

## Disclosure Timeline

- 2022-01-21 - Vulnerability reported to vendor
- 2022-03-23 - Coordinated public release of advisory
