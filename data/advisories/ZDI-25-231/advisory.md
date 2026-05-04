# ZDI-25-231: Luxion KeyShot SKP File Parsing Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-231
- **ZDI-CAN:** ZDI-CAN-23646
- **Date:** 2025-04-09
- **CVE:** CVE-2025-1046
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Luxion
- **Affected Products:** KeyShot
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-231/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Luxion KeyShot. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of SKP files. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Luxion has issued an update to correct this vulnerability. More details can be found at: https://download.keyshot.com/cert/ksa-113962/ksa-113962.pdf?version=1.0&_gl=1*1x6i3a*_gcl_au*MTU0ODMwNDI4Ny4xNzQzNTUyMjcx

## Disclosure Timeline

- 2024-09-11 - Vulnerability reported to vendor
- 2025-04-09 - Coordinated public release of advisory
- 2025-04-09 - Advisory Updated
