# ZDI-24-1121: Apple macOS VideoToolbox Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1121
- **ZDI-CAN:** ZDI-CAN-23591
- **Date:** 2024-08-08
- **CVE:** CVE-2024-27829
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Pwn2car
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1121/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Apple macOS. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of MOV files in the VTDecoderXPCService process. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-ca/HT214106

## Disclosure Timeline

- 2024-05-01 - Vulnerability reported to vendor
- 2024-08-08 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
