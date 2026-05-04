# ZDI-20-674: Apple macOS AudioToolboxCore CAF File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-674
- **ZDI-CAN:** ZDI-CAN-10652
- **Date:** 2020-05-27
- **CVE:** CVE-2020-9815
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Yu Zhou(@yuzhou6666) of \xe5\xb0\x8f\xe9\xb8\xa1\xe5\xb8\xae
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-674/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apple macOS. Interaction with the AudioToolbox library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the AudioToolbox framework. Crafted data in a CAF file can trigger a write past the end of an allocated data structure. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

https://support.apple.com/en-gb/HT211170

## Disclosure Timeline

- 2020-04-28 - Vulnerability reported to vendor
- 2020-05-27 - Coordinated public release of advisory
