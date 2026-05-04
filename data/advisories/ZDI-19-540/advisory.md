# ZDI-19-540: Apple Safari cfAttributedStringUnserialize Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-540
- **ZDI-CAN:** ZDI-CAN-8366
- **Date:** 2019-05-30
- **CVE:** CVE-2019-8603
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** phoenhex & qwerty team (@_niklasb @qwertyoruiopz and @bkth_)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-540/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the cfAttributedStringUnserialize method. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT210119

## Disclosure Timeline

- 2019-05-17 - Vulnerability reported to vendor
- 2019-05-30 - Coordinated public release of advisory
