# ZDI-20-800: (Pwn2Own) ICONICS Genesis64 PKGX Improper Verification of Cryptographic Signature Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-800
- **ZDI-CAN:** ZDI-CAN-10273
- **Date:** 2020-07-01
- **CVE:** N/A
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** ICONICS
- **Affected Products:** Genesis64
- **Credit:** ZDIcases
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-800/
## Vulnerability Details

The vulnerablity allows remote attackers to execute arbitrary code on affected installations of ICONICS Genesis64. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of PKGX files. The application fails to validate the cryptographic signature of the package. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

ICONICS has issued an update to correct this vulnerability. More details can be found at: https://www.us-cert.gov/ics/advisories/icsa-20-170-04

## Disclosure Timeline

- 2020-06-30 - Vulnerability reported to vendor
- 2020-07-01 - Coordinated public release of advisory
