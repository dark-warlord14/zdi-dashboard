# ZDI-23-644: Apple GarageBand MIDI File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-644
- **ZDI-CAN:** ZDI-CAN-17199
- **Date:** 2023-05-17
- **CVE:** CVE-2023-27938
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** GarageBand
- **Credit:** Mickey Jin (@patch1t) of Trend Micro
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-644/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Apple GarageBand. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within a function in MACore.framework. Crafted data in a MIDI file can trigger a read past the end of an allocated data structure. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/HT213650

## Disclosure Timeline

- 2022-04-27 - Vulnerability reported to vendor
- 2023-05-17 - Coordinated public release of advisory
