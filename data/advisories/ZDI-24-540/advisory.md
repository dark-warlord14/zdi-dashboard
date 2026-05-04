# ZDI-24-540: Luxion KeyShot BIP File Parsing Uncontrolled Search Path Element Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-540
- **ZDI-CAN:** ZDI-CAN-22738
- **Date:** 2024-05-31
- **CVE:** CVE-2024-5509
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Luxion
- **Affected Products:** KeyShot
- **Credit:** Sean de Regge
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-540/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Luxion KeyShot. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of BIP files. The issue results from loading a library from an unsecured location. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Luxion has issued an update to correct this vulnerability. More details can be found at: https://www.keyshot.com/csirt/

## Disclosure Timeline

- 2024-01-03 - Vulnerability reported to vendor
- 2024-05-31 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
