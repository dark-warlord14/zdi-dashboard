# ZDI-25-648: Anritsu ShockLine CHX File Parsing Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-648
- **ZDI-CAN:** ZDI-CAN-26882
- **Date:** 2025-07-24
- **CVE:** CVE-2025-7976
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Anritsu
- **Affected Products:** ShockLine
- **Credit:** kimiya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-648/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Anritsu ShockLine. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of CHX files. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in ShockLine version: 2025.4.2 https://www.anritsu.com/en-us/test-measurement/support/downloads/software/dwl18844

## Disclosure Timeline

- 2025-05-15 - Vulnerability reported to vendor
- 2025-07-24 - Coordinated public release of advisory
- 2025-07-24 - Advisory Updated
