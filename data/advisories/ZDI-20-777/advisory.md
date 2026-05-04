# ZDI-20-777: (Pwn2Own) ICONICS Genesis64 PKGX WbPackAndGoSettings Absolute Path Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-777
- **ZDI-CAN:** ZDI-CAN-10272
- **Date:** 2020-06-30
- **CVE:** CVE-2020-12009
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** ICONICS
- **Affected Products:** Genesis64
- **Credit:** Team FLASHBACK: Pedro Ribeiro (pedrib@gmail.com|@pedrib1337) and Radek Domanski (@RabbitPro)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-777/
## Vulnerability Details

The vulnerablity allows remote attackers to execute arbitrary code on affected installations of ICONICS Genesis64. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of PKGX files. When parsing the WbPackAndGoSettings element, the process does not properly validate a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

ICONICS has issued an update to correct this vulnerability. More details can be found at: https://www.us-cert.gov/ics/advisories/icsa-20-170-03

## Disclosure Timeline

- 2020-06-23 - Vulnerability reported to vendor
- 2020-06-30 - Coordinated public release of advisory
