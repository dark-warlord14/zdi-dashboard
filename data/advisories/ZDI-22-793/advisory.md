# ZDI-22-793: Apple Safari WebGL generateMipmap Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-793
- **ZDI-CAN:** ZDI-CAN-16206
- **Date:** 2022-05-26
- **CVE:** CVE-2022-26748
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-793/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the WebGL library. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT213257

## Disclosure Timeline

- 2022-03-02 - Vulnerability reported to vendor
- 2022-05-26 - Coordinated public release of advisory
- 2024-07-08 - Advisory Updated
