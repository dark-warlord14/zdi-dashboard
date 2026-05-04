# ZDI-24-032: Foxit PDF Reader Doc Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-032
- **ZDI-CAN:** ZDI-CAN-22109
- **Date:** 2024-01-10
- **CVE:** N/A
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Foxit
- **Affected Products:** PDF Reader
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-032/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Foxit PDF Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of Doc objects. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in Foxit PDF Reader version v12.1.3. https://www.foxit.com/support/security-bulletins.html

## Disclosure Timeline

- 2023-10-03 - Vulnerability reported to vendor
- 2024-01-10 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
