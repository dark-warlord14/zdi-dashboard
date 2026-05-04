# ZDI-13-021: Adobe Flash Player loadPCMFromByteArray Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-021
- **ZDI-CAN:** ZDI-CAN-1582
- **Date:** 2013-02-11
- **CVE:** CVE-2012-5677
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Flash Player
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-021/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Flash Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the loadPCMFromByteArray function in the flash.media.Sound object. When this function is called with a high number of 'samples' an integer overflow occurs during the calculation of a buffer size. This can lead to memory corruption that can result in remote code execution under the context of the current user.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb12-27.html

## Disclosure Timeline

- 2012-10-24 - Vulnerability reported to vendor
- 2013-02-11 - Coordinated public release of advisory
