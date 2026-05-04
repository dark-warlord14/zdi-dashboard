# ZDI-09-066: Adobe RoboHelp Server Arbitrary File Upload and Execute Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-066
- **ZDI-CAN:** ZDI-CAN-504
- **Date:** 2009-09-23
- **CVE:** CVE-2009-3068
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Adobe
- **Affected Products:** RoboHelp Server
- **Credit:** Stephen Fewer of Harmony Security (www.harmonysecurity.com)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-066/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerability installations of Adobe RoboHelp Server. Authentication is not required to exploit this vulnerability. The specific flaw exists in the management web server listening by default on port 8080. The Java Servlet handling POST requests to the server does not properly sanitize user input. A specially crafted request can bypass authentication allowing an attacker to upload and execute arbitrary files. Successful exploitation can result in complete system compromise under SYSTEM credentials.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb09-14.html

## Disclosure Timeline

- 2009-06-26 - Vulnerability reported to vendor
- 2009-09-23 - Coordinated public release of advisory
