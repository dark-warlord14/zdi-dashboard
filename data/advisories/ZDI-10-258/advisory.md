# ZDI-10-258: Apple QuickTime 3GP Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-258
- **ZDI-CAN:** ZDI-CAN-645
- **Date:** 2010-12-07
- **CVE:** CVE-2010-1508
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Moritz Jodeit of n.runs AG
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-258/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Quicktime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the Quicktime.qts module responsible for parsing media files. While handling 3GP streams a function within this module a loop trusts a value directly from the media file and uses it during memory copy operations. By supplying a large enough value this buffer can be overflowed leading to arbitrary code execution under the context of the user accessing the file.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT4447

## Disclosure Timeline

- 2010-01-06 - Vulnerability reported to vendor
- 2010-12-07 - Coordinated public release of advisory
