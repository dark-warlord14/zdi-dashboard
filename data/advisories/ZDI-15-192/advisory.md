# ZDI-15-192: Hewlett-Packard Network Virtualization Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-192
- **ZDI-CAN:** ZDI-CAN-2569
- **Date:** 2015-05-12
- **CVE:** CVE-2015-2121
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:N/A:N
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Network Virtualization
- **Credit:** Aniway.Anyway@gmail.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-192/
## Vulnerability Details

This vulnerability allows remote attackers to read arbitrary files on vulnerable installations of Hewlett-Packard Network Virtualization. Authentication is not required to exploit this vulnerability. The specific flaw exists because neither the HttpServlet nor the NetworkEditorController sanitize the URL, and hence the file name, requested. An attacker can use this to read any file on the system under the context of SYSTEM.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c04657310

## Disclosure Timeline

- 2015-02-04 - Vulnerability reported to vendor
- 2015-05-12 - Coordinated public release of advisory
