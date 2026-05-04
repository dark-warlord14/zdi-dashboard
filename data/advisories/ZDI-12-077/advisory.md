# ZDI-12-077: Apple QuickTime QTVR QTVRStringAtom Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-077
- **ZDI-CAN:** ZDI-CAN-1422
- **Date:** 2012-06-06
- **CVE:** CVE-2012-0667
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Alin Rad Pop
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-077/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the QuickTimeVR.qtx component. A signedness error exists when processing a QTVRStringAtom having an overly large "stringLength" parameter. This can be exploited to cause a stack-based buffer overflow and execute arbitrary code under the context of the user running the application.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT5261

## Disclosure Timeline

- 2011-10-21 - Vulnerability reported to vendor
- 2012-06-06 - Coordinated public release of advisory
