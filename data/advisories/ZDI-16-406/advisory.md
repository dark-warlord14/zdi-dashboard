# ZDI-16-406: Novell NetIQ Sentinel Server ReportViewServlet fileName Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-406
- **ZDI-CAN:** ZDI-CAN-3717
- **Date:** 2016-07-07
- **CVE:** CVE-2016-1605
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:L/Au:S/C:C/I:N/A:N
- **Affected Vendors:** Novell
- **Affected Products:** NetIQ Sentinel
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-406/
## Vulnerability Details

This vulnerability allows remote attackers to disclose arbitrary file contents on vulnerable installations of Novell NetIQ Sentinel Server. Authentication is required to exploit this vulnerability but it can be bypassed using a separate flaw within the LogonFormController. The specific flaw exists within the ReportViewServlet servlet. When fileType is specified as "PREVIEW", the fileName parameter is vulnerable to directory traversal. An attacker could leverage this vulnerability to read the content of arbitrary files from the system.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: https://www.netiq.com/support/kb/doc.php?id=7017803

## Disclosure Timeline

- 2016-05-09 - Vulnerability reported to vendor
- 2016-07-07 - Coordinated public release of advisory
