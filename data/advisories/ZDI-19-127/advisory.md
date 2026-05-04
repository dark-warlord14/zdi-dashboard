# ZDI-19-127: Apple Safari RTCPeerConnection Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-127
- **ZDI-CAN:** ZDI-CAN-7481
- **Date:** 2019-01-25
- **CVE:** CVE-2019-6211
- **CVSS:** 6.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:L
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** MWR
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-127/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of RTCPeerConnection objects. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/kb/HT201222

## Disclosure Timeline

- 2018-11-08 - Vulnerability reported to vendor
- 2019-01-25 - Coordinated public release of advisory
