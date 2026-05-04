# ZDI-08-003: Symantec Backup Exec Remote File Upload Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-003
- **ZDI-CAN:** ZDI-CAN-253
- **Date:** 2008-02-06
- **CVE:** CVE-2008-0457
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Symantec
- **Affected Products:** Backup Exec System Recovery Manager
- **Credit:** Titon of BastardLabs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-003/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Symantec Backup Exec System Recovery Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists in the FileUpload class running on the Symantec LiveState Apache Tomcat server. The server is found on TCP ports 8080 and 8443. A malicious HTTP POST request can upload a JSP script to the publicly accessible web directories allowing for arbitrary code execution.

## Additional Details

Symantec has issued an update to correct this vulnerability. More details can be found at: http://www.symantec.com/avcenter/security/Content/2008.02.04.html

## Disclosure Timeline

- 2007-12-11 - Vulnerability reported to vendor
- 2008-02-06 - Coordinated public release of advisory
