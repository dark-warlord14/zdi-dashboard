# ZDI-24-1288: Apple macOS AppleIntelKBLGraphicsMTLDriver Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1288
- **ZDI-CAN:** ZDI-CAN-24088
- **Date:** 2024-09-25
- **CVE:** CVE-2024-40846
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Michael DePlante (@izobashi) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1288/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apple macOS. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the AppleIntelKBLGraphicsMTLDriver. Crafted texture data can trigger a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/121238

## Disclosure Timeline

- 2024-05-21 - Vulnerability reported to vendor
- 2024-09-25 - Coordinated public release of advisory
- 2024-09-25 - Advisory Updated
