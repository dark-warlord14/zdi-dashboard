# ZDI-16-035: Oracle Application Testing Suite Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-035
- **ZDI-CAN:** ZDI-CAN-3324
- **Date:** 2016-01-25
- **CVE:** CVE-2016-0488
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Oracle
- **Affected Products:** Application Testing Suite
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-035/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on vulnerable installations of Oracle Application Testing Suite. The specific flaw exists within the isAllowedUrl() function used for the admin pages. This function has a list of URI entries which do not require authentication. Because the function only checks to see if a URI starts with one of these entries, an attacker can use directory traversal in the URI to gain access to all of the exposed administrator functionality.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/cpujan2016-2367955.html

## Disclosure Timeline

- 2015-10-08 - Vulnerability reported to vendor
- 2016-01-25 - Coordinated public release of advisory
