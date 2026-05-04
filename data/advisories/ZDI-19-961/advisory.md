# ZDI-19-961: Apple macOS AudioToolbox Interleave Out-of-Bounds Write Remote Code Execute Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-961
- **ZDI-CAN:** ZDI-CAN-8160
- **Date:** 2019-11-01
- **CVE:** N/A
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** riusksk of VulWar Corp
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-961/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple macOS. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the AudioToolbox module. Crafted data in an AU file can trigger a write past the end of an allocated data structure. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT210119

## Disclosure Timeline

- 2019-03-28 - Vulnerability reported to vendor
- 2019-11-01 - Coordinated public release of advisory
