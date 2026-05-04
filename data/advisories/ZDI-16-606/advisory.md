# ZDI-16-606: CA Unified Infrastructure Management get_sessions Session Information Disclosure Remote Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-606
- **ZDI-CAN:** ZDI-CAN-3708
- **Date:** 2016-11-09
- **CVE:** CVE-2016-9165
- **CVSS:** 5.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:N/A:N
- **Affected Vendors:** CA
- **Affected Products:** Unified Infrastructure Management
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-606/
## Vulnerability Details

This vulnerability allows remote attackers to disclose session information on vulnerable installations of CA Unified Infrastructure Management. Authentication is not required to exploit this vulnerability. The specific flaw exists within processing of the get_sessions servlet. The servlet can return the session IDs for all active sessions. An attacker can use this information to hijack any current active session, including administrative sessions.

## Additional Details

CA has issued an update to correct this vulnerability. More details can be found at: http://www.ca.com/us/services-support/ca-support/ca-support-online/product-content/recommended-reading/security-notices/ca20161109-01-security-notice-for-ca-unified-infrastructure-mgmt.html

## Disclosure Timeline

- 2016-04-28 - Vulnerability reported to vendor
- 2016-11-09 - Coordinated public release of advisory
