# ZDI-15-331: Microsoft Internet Explorer Enhanced Protected Mode Read-Restrictions Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-331
- **ZDI-CAN:** ZDI-CAN-2863
- **Date:** 2015-07-14
- **CVE:** CVE-2015-2412
- **CVSS:** 4.7
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Ashutosh Mehra (https://twitter.com/ashutoshmehra)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-331/
## Vulnerability Details

This vulnerability allows remote attackers to partially escape AppContainer limitations on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the IE broker process when processing a file name for reading in the routine IShdocvwBroker::MOTWCreateFileW. Using a directory junction and a symbolic link, code running inside the EPM AppContainer can read any file that the normal user account can read, bypassing the restrictions designed into EPM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/MS15-065

## Disclosure Timeline

- 2015-04-07 - Vulnerability reported to vendor
- 2015-07-14 - Coordinated public release of advisory
