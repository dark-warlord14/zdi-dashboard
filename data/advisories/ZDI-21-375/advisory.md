# ZDI-21-375: Apple macOS AudioCodecs MP4 File Parsing Signed to Unsigned Conversion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-375
- **ZDI-CAN:** ZDI-CAN-11448
- **Date:** 2021-03-30
- **CVE:** CVE-2020-27908
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-375/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apple macOS. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the AudioCodecs module. Crafted data in an MP4 file can trigger a write outside the bounds of an allocated data structure. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT211928

## Disclosure Timeline

- 2020-09-16 - Vulnerability reported to vendor
- 2021-03-30 - Coordinated public release of advisory
