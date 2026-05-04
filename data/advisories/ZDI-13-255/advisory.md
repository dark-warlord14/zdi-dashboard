# ZDI-13-255: Cisco Data Center Network Manager fileUploadServlet Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-255
- **ZDI-CAN:** ZDI-CAN-1767
- **Date:** 2013-11-24
- **CVE:** CVE-2013-5486
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Cisco
- **Affected Products:** Data Center Network Manager
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-255/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Cisco Data Center Network Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the FileUploadServlet. Multiple arguments of a multipart form request are vulnerable to directory traversal attacks. A remote attacker can abuse this to execute remote code under the context of the SYSTEM user.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: http://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20130918-dcnm

## Disclosure Timeline

- 2013-02-22 - Vulnerability reported to vendor
- 2013-11-24 - Coordinated public release of advisory
