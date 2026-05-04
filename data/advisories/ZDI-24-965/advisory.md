# ZDI-24-965: Apple macOS VideoToolbox Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-965
- **ZDI-CAN:** ZDI-CAN-23325
- **Date:** 2024-07-26
- **CVE:** CVE-2024-27829
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Pwn2car
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-965/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apple macOS. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of MOV files in the VTDecoderXPCService process. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT214106

## Disclosure Timeline

- 2024-03-08 - Vulnerability reported to vendor
- 2024-07-26 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
