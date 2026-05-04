# ZDI-11-038: Apple Quicktime Sprite Transformation Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-038
- **ZDI-CAN:** ZDI-CAN-910
- **Date:** 2011-02-01
- **CVE:** CVE-2010-3790
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-038/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Quicktime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within how the application performs a transformation on an image sample using the sprite handler. When performing the transformation, the application will scale the sprite outside the bounds of the original buffer. This can cause memory corruption which can lead to code execution within the context of the application.

## Additional Details

http://support.apple.com/kb/HT4435 and http://support.apple.com/kb/HT4447

## Disclosure Timeline

- 2010-11-05 - Vulnerability reported to vendor
- 2011-02-01 - Coordinated public release of advisory
