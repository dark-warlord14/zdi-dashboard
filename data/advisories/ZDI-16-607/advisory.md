# ZDI-16-607: CA Unified Infrastructure Management diag Path Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-607
- **ZDI-CAN:** ZDI-CAN-3710
- **Date:** 2016-11-09
- **CVE:** CVE-2016-9164
- **CVSS:** 5.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:N/A:N
- **Affected Vendors:** CA
- **Affected Products:** Unified Infrastructure Management
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-607/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information from vulnerable installations of CA Unified Infrastructure Management. Authentication is not required to exploit this vulnerability. The specific flaw exists within processing of the diag.jsp servlet. The servlet is vulnerable to directory traversal and can be used to exfiltrate sensitive system files from the system.

## Additional Details

CA has issued an update to correct this vulnerability. More details can be found at: http://www.ca.com/us/services-support/ca-support/ca-support-online/product-content/recommended-reading/security-notices/ca20161109-01-security-notice-for-ca-unified-infrastructure-mgmt.html

## Disclosure Timeline

- 2016-04-28 - Vulnerability reported to vendor
- 2016-11-09 - Coordinated public release of advisory
