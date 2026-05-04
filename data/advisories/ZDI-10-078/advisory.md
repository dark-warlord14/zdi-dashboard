# ZDI-10-078: Novell ZENworks Configuration Management UploadServlet Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-078
- **ZDI-CAN:** ZDI-CAN-678
- **Date:** 2010-04-23
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Novell
- **Affected Products:** Zenworks
- **Credit:** Stephen Fewer of Harmony Security (www.harmonysecurity.com)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-078/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell ZENworks. Authentication is not required to exploit this vulnerability. The specific flaw exists within the ZENworks Server (zenserver.exe). This Tomcat server listens by default on TCP ports 80 and 443. The vulnerability exists in the UploadServlet. Using the UploadServlet an attacker can upload a malicious file outside of the TEMP directory on the server. By accessing this uploaded file remotely it is executed in the context of the zenserver.exe process. This can be exploited to gain arbitrary code execution in the context of the user running the ZENworks server.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://www.novell.com/support/viewContent.do?externalId=7005573

## Disclosure Timeline

- 2010-02-09 - Vulnerability reported to vendor
- 2010-04-23 - Coordinated public release of advisory
