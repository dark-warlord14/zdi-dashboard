# ZDI-06-021: WebEx Downloader Plug-in Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-06-021
- **ZDI-CAN:** ZDI-CAN-034
- **Date:** 2006-07-06
- **CVE:** CVE-2006-3423
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** WebEx Communications Inc.
- **Affected Products:** Web Conference ActiveX Control
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-06-021/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of the WebEx Downloader Plug-in. Successful exploitation requires that the target user browse to a malicious web page. The specific flaws exists due to the lack of input validation on various ActiveX/Java control parameters and configuration directives. The "GpcUrlRoot" and "GpcIniFileName" ActiveX/Java control parameters allow an attacker to specify the location of a configuration file containing further control directives. This allows an attacker to transfer arbitrary files and executables to the target. The attacker can then leverage available configuration directives to execute the newly created executables thereby compromising the underlying system.

## Additional Details

WebEx Communications Inc. has issued an update to correct this vulnerability. More details can be found at: http://www.webex.com/lp/security/ActiveAdv.html?TrackID=123456

## Disclosure Timeline

- 2006-04-11 - Vulnerability reported to vendor
- 2006-07-06 - Coordinated public release of advisory
