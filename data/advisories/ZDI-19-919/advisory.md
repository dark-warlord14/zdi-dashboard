# ZDI-19-919: Apple macOS AudioCodecs Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-919
- **ZDI-CAN:** ZDI-CAN-8093
- **Date:** 2019-10-25
- **CVE:** CVE-2019-8592
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** riusksk of VulWar Corp
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-919/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple macOS. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the AudioCodecs module. Crafted data in a MOV file can trigger a write past the end of an allocated data structure. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT210119

## Disclosure Timeline

- 2019-03-14 - Vulnerability reported to vendor
- 2019-10-25 - Coordinated public release of advisory
