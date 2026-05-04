# ZDI-15-279: Apple QuickTime GIF Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-279
- **ZDI-CAN:** ZDI-CAN-2685
- **Date:** 2015-07-01
- **CVE:** CVE-2015-3663
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** QuickTime
- **Credit:** kdot
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-279/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of GIF images. By providing a GIF with a malformed image descriptor, an attacker can write data outside the bounds of the data structure. An attacker could leverage this to execute arbitrary code in the context of the QuickTime process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT201222

## Disclosure Timeline

- 2015-02-04 - Vulnerability reported to vendor
- 2015-07-01 - Coordinated public release of advisory
