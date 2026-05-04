# ZDI-21-913: Foxit Reader embedDocAsDataObject Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-913
- **ZDI-CAN:** ZDI-CAN-13741
- **Date:** 2021-07-30
- **CVE:** CVE-2021-34831
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Foxit
- **Affected Products:** Reader
- **Credit:** Xu Peng from UCAS and Wang Yanhao from QiAnXin Technology Research Institute
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-913/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Foxit Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of Document objects. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxit.com/support/security-bulletins.html

## Disclosure Timeline

- 2021-05-13 - Vulnerability reported to vendor
- 2021-07-30 - Coordinated public release of advisory
- 2021-08-03 - Advisory Updated
