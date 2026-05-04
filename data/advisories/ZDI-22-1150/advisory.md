# ZDI-22-1150: Omron CX-One CX-Programmer CXP File Parsing Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1150
- **ZDI-CAN:** ZDI-CAN-15341
- **Date:** 2022-08-23
- **CVE:** N/A
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Omron
- **Affected Products:** CX-One
- **Credit:** xina1i
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1150/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Omron CX-One. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of CXP files in the CX-Programmer module. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Omron has issued an update to correct this vulnerability. More details can be found at: https://www.ia.omron.com/product/tool/26/cxone/e4_doc.html

## Disclosure Timeline

- 2021-12-15 - Vulnerability reported to vendor
- 2022-08-23 - Coordinated public release of advisory
