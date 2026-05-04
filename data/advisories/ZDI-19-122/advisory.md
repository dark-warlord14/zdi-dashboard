# ZDI-19-122: Apple Safari RenderBlockFlow Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-122
- **ZDI-CAN:** ZDI-CAN-7205
- **Date:** 2019-01-25
- **CVE:** CVE-2019-6233
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** WebKit
- **Credit:** G. Geshev from MWR Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-122/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of RenderBlockFlow objects. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/kb/HT201222

## Disclosure Timeline

- 2018-09-03 - Vulnerability reported to vendor
- 2019-01-25 - Coordinated public release of advisory
