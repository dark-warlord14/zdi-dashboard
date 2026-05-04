# ZDI-10-260: Apple QuickTime Panorama Atom Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-260
- **ZDI-CAN:** ZDI-CAN-734
- **Date:** 2010-12-07
- **CVE:** CVE-2010-3802
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-260/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Quicktime. User interaction is required to exploit this vulnerability in that a user must be coerced into visiting a malicious page or opening a malicious file. The specific flaw exists within Apple's support for Panoramic Images and occurs due to the application trusting a particular field for calculation of an offset. Due to the field being treated as a signed integer, the calculated offset can result in a pointer outside the bounds of the expected buffer. Upon usage of this out-of-bounds pointer, the application will write proceed to write image data to the invalid location. Successful exploitation can lead to code execution under the context of the application.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT4447

## Disclosure Timeline

- 2010-03-22 - Vulnerability reported to vendor
- 2010-12-07 - Coordinated public release of advisory
