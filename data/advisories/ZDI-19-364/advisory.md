# ZDI-19-364: (Pwn2Own) Mozilla Firefox Array.slice Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-364
- **ZDI-CAN:** ZDI-CAN-8368
- **Date:** 2019-04-15
- **CVE:** CVE-2019-9810
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Mozilla
- **Affected Products:** Firefox
- **Credit:** fluoroacetate (@fluoroacetate)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-364/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the implementation of Array.slice when executed within JIT compiled code. By performing actions in JavaScript, an attacker can trigger a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Mozilla has issued an update to correct this vulnerability. More details can be found at: https://www.mozilla.org/en-US/security/advisories/mfsa2019-09/#CVE-2019-9810

## Disclosure Timeline

- 2019-03-21 - Vulnerability reported to vendor
- 2019-04-15 - Coordinated public release of advisory
- 2019-06-14 - Advisory Updated
