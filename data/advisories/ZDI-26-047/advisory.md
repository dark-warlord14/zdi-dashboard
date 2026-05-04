# ZDI-26-047: Hancom Office DOC File Parsing Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-047
- **ZDI-CAN:** ZDI-CAN-26620
- **Date:** 2026-01-28
- **CVE:** CVE-2025-29867
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Hancom
- **Affected Products:** Office
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-047/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Hancom Office. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of DOC files. The issue results from the lack of proper validation of user-supplied data, which can result in a type confusion condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in Word Version: 11.0.0.8916

## Disclosure Timeline

- 2025-08-14 - Vulnerability reported to vendor
- 2026-01-28 - Coordinated public release of advisory
- 2026-01-28 - Advisory Updated
