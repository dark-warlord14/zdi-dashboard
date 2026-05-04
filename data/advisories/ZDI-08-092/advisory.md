# ZDI-08-092: Adobe Flash Script Injection Cross Domain Scripting Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-092
- **ZDI-CAN:** ZDI-CAN-268
- **Date:** 2008-04-08
- **CVE:** CVE-2007-6637
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Adobe
- **Affected Products:** Flash Player
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-092/
## Vulnerability Details

This vulnerability allows remote attackers to inject scripts across domains through vulnerable versions of Adobe Flash. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists in the handling of scripts injected via Flash's redirect methods over both the data: and javascript: protocol handlers. Both cases result in the browser incorrectly executing the script code under the context of the redirecting hostname. The flashContentURL parameter to flash_detection.swf is a popular and widespread example of a vulnerable SWF file which can be abused.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb08-11.html

## Disclosure Timeline

- 2008-01-10 - Vulnerability reported to vendor
- 2008-04-08 - Coordinated public release of advisory
