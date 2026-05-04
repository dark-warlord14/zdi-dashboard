# ZDI-07-037: Microsoft Internet Explorer Language Pack Installation Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-037
- **ZDI-CAN:** ZDI-CAN-119
- **Date:** 2007-06-12
- **CVE:** CVE-2007-3027
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-037/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists in routines responsible for the on-demand installation of Internet Explorer language packs. A race condition may occur when a web page contains several pieces of content written in a language not currently supported by any of the installed language packs. In some cases, this race condition results in exploitable memory corruption that can be leveraged to execute arbitrary code.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/ms07-033.mspx

## Disclosure Timeline

- 2006-11-08 - Vulnerability reported to vendor
- 2007-06-12 - Coordinated public release of advisory
