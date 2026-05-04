# ZDI-12-076: Apple QuickTime MPEG Stream Padding Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-076
- **ZDI-CAN:** ZDI-CAN-1376
- **Date:** 2012-06-06
- **CVE:** CVE-2012-0659
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Anonymous pa_kt / twitter.com/pa_kt / e1c14ba6
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-076/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple's QuickTime Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within how the application calculates the padding for an MPEG sample. When calculating the padding, the MPEG library will subtract this from another length without checking for underflow. This resulting length will then be used in a memcpy operation into a statically sized buffer allocated on the heap. This can lead to code execution under the context of the application.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT5261

## Disclosure Timeline

- 2011-10-21 - Vulnerability reported to vendor
- 2012-06-06 - Coordinated public release of advisory
