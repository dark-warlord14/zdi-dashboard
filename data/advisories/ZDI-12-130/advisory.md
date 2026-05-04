# ZDI-12-130: Apple QuickTime Player MP4A Uninitialized Pointer Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-130
- **ZDI-CAN:** ZDI-CAN-1382
- **Date:** 2012-08-03
- **CVE:** CVE-2011-3458
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** QuickTime
- **Credit:** Luigi Auriemma pa_kt / twitter.com/pa_kt / e1c14ba6
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-130/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within how the application parses a header containing codec-specific data. When handling an error case, the application will forget to initialize a pointer which will later be used in a memory operation. This can lead to code execution under the context of the application.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT1222

## Disclosure Timeline

- 2011-10-21 - Vulnerability reported to vendor
- 2012-08-03 - Coordinated public release of advisory
