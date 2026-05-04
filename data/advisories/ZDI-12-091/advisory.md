# ZDI-12-091: Symantec Web Gateway upload_file Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-091
- **ZDI-CAN:** ZDI-CAN-1436
- **Date:** 2012-06-08
- **CVE:** CVE-2012-0299
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Symantec
- **Affected Products:** Web Gateway
- **Credit:** Tenable Network Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-091/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Symantec Web Gateway. Authentication is not required to exploit this vulnerability. The specific flaw exists because Symantec Web Gateway allows unauthenticated users to upload a file while preserving the file extension. This allows users to upload additional script files that can be used to execute remote code from user supplied commands under the context of the webserver.

## Additional Details

Symantec has issued an update to correct this vulnerability. More details can be found at: http://www.symantec.com/security_response/securityupdates/detail.jsp?fid=security_advisory&pvid=security_advisory&year=2012&suid=20120517_00

## Disclosure Timeline

- 2011-11-22 - Vulnerability reported to vendor
- 2012-06-08 - Coordinated public release of advisory
