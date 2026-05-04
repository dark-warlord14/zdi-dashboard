# ZDI-11-126: CA Total Defense Suite Heartbeat Web Service Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-126
- **ZDI-CAN:** ZDI-CAN-1001
- **Date:** 2011-04-13
- **CVE:** CVE-2011-1654
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** CA
- **Affected Products:** Total Defense Suite
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-126/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of CA Total Defense Endpoint. Authentication is not required to exploit this vulnerability. The specific flaw exists within CA.Itm.Server.ManagementWS.dll. Due to a failure to properly sanitize user-controlled input, it is possible for a remote unauthenticated attacker to upload and subsequently execute arbitrary code under the context of the CA Total Defense Heartbeat Web service. Requests delivered to FileUploadHandler.ashx are subject to arbitrary file writes, including directory traversal attacks, in the GUID parameter. The Heartbeat Web service listens for HTTP requests on port 8008 and 44344 for HTTPS.

## Additional Details

CA has issued an update to correct this vulnerability. More details can be found at: https://support.ca.com/irj/portal/anonymous/phpsupcontent?contentID={CD065CEC-AFE2-4D9D-8E0B-BE7F6E345866}

## Disclosure Timeline

- 2011-01-21 - Vulnerability reported to vendor
- 2011-04-13 - Coordinated public release of advisory
