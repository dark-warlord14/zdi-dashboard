# ZDI-19-863: Apple macOS CFFromShiftJISLen Out-Of-Bounds Read Remote Code Execution

## Metadata

- **ZDI ID:** ZDI-19-863
- **ZDI-CAN:** ZDI-CAN-8588
- **Date:** 2019-10-08
- **CVE:** CVE-2019-8745
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** riusksk of VulWar Corp
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-863/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apple macOS. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the CFFromShiftJISLen function. Crafted data in a DOC file can trigger a read past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT210634

## Disclosure Timeline

- 2019-05-31 - Vulnerability reported to vendor
- 2019-10-08 - Coordinated public release of advisory
