# ZDI-09-092: Adobe Flash Player JPEG Parsing Heap Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-092
- **ZDI-CAN:** ZDI-CAN-517
- **Date:** 2009-12-09
- **CVE:** CVE-2009-3794
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Adobe
- **Affected Products:** Flash Player
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-092/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Flash Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious web page or open a malicious SWF file. The specific flaw exists in the parsing of JPEG dimensions contained within an SWF file. Due to the lack of sanity checking when calculating the frame size of an image it is possible to overflow a heap based buffer. Successful exploitation of this issue can lead to remote system compromise under the credentials of the currently logged in user.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb09-19.html

## Disclosure Timeline

- 2009-07-14 - Vulnerability reported to vendor
- 2009-12-09 - Coordinated public release of advisory
