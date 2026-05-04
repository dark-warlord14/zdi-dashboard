# ZDI-20-1391: Apple macOS AudioToolboxCore Wave Header Parsing Sign Extension Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1391
- **ZDI-CAN:** ZDI-CAN-11189
- **Date:** 2020-12-03
- **CVE:** CVE-2020-9889
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1391/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apple macOS. Interaction with the AudioToolbox library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the AudioToolbox framework. Crafted data in a WAV file can trigger a sign extension before allocating a buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT211289

## Disclosure Timeline

- 2020-07-01 - Vulnerability reported to vendor
- 2020-12-03 - Coordinated public release of advisory
