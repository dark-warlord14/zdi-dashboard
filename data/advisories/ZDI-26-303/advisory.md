# ZDI-26-303: Foxit PDF Reader AcroForm Signature Use-After-Free Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-303
- **ZDI-CAN:** ZDI-CAN-29494
- **Date:** 2026-04-27
- **CVE:** CVE-2026-5942
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Foxit
- **Affected Products:** PDF Reader
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-303/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Foxit PDF Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of Signature objects. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxit.com/support/security-bulletins.html

## Disclosure Timeline

- 2026-03-30 - Vulnerability reported to vendor
- 2026-04-27 - Coordinated public release of advisory
- 2026-04-27 - Advisory Updated
