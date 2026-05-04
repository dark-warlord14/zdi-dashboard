# ZDI-16-605: CA Unified Infrastructure Management download_lar Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-605
- **ZDI-CAN:** ZDI-CAN-3711
- **Date:** 2016-11-09
- **CVE:** CVE-2016-5803
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:N/A:N
- **Affected Vendors:** CA
- **Affected Products:** Unified Infrastructure Management
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-605/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information from vulnerable installations of CA Unified Infrastructure Management. Authentication is not required to exploit this vulnerability. The specific flaw exists within processing of the download_lar servlet. The servlet is vulnerable to directory traversal and can be used to exfiltrate sensitive system files from the system.

## Additional Details

CA has issued an update to correct this vulnerability. More details can be found at: http://www.ca.com/us/services-support/ca-support/ca-support-online/product-content/recommended-reading/security-notices/ca20161109-01-security-notice-for-ca-unified-infrastructure-mgmt.html

## Disclosure Timeline

- 2016-08-30 - Vulnerability reported to vendor
- 2016-11-09 - Coordinated public release of advisory
