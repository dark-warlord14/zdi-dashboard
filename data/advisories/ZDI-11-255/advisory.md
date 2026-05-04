# ZDI-11-255: Apple QuickTime Player H.264 Reference Picture List Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-255
- **ZDI-CAN:** ZDI-CAN-1232
- **Date:** 2011-08-16
- **CVE:** CVE-2011-0247
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Roi Mallo & Sherab Giovannini
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-255/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within how the application parses a frame within an H.264 encoded movie. When processing a particular set of flags of a structure, the application will use a length that is defined within the structure to copy data into a statically sized buffer on the stack. Due to the application failing to check the bounds of this length, the application will write outside the bounds of the buffer which can lead to code execution under the context of the application.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT4826

## Disclosure Timeline

- 2011-05-12 - Vulnerability reported to vendor
- 2011-08-16 - Coordinated public release of advisory
