# ZDI-20-1396: Apple macOS AudioCodecs AAC Decoding Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1396
- **ZDI-CAN:** ZDI-CAN-11507
- **Date:** 2020-12-04
- **CVE:** CVE-2020-10017
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Francis
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1396/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apple macOS. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the AudioCodecs module. Crafted AAC data in an MP4 file can trigger a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT211931

## Disclosure Timeline

- 2020-08-05 - Vulnerability reported to vendor
- 2020-12-04 - Coordinated public release of advisory
