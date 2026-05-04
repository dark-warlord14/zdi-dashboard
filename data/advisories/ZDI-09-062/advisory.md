# ZDI-09-062: Microsoft Internet Explorer JScript arguments Invocation Memory Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-062
- **ZDI-CAN:** ZDI-CAN-482
- **Date:** 2009-09-08
- **CVE:** CVE-2009-1920
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** ling&wushi of team509
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-062/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists when parsing the jscript keyword "arguments". Because the arguments object is not available until a certain time, invoking it can result in memory corruption. Successful exploitation of this vulnerability can lead to a remote system compromise under the credentials of the current user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/ms09-045.mspx

## Disclosure Timeline

- 2009-04-28 - Vulnerability reported to vendor
- 2009-09-08 - Coordinated public release of advisory
