# ZDI-07-060: Hewlett-Packard OpenView Radia Integration Server File System Exposure Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-060
- **ZDI-CAN:** ZDI-CAN-134
- **Date:** 2007-10-31
- **CVE:** CVE-2007-5413
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** OpenView Radia Integration Server
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-060/
## Vulnerability Details

This vulnerability allows remote attackers to access arbitrary files on systems with vulnerable installations of Hewlett-Packard OpenView Radia Integration Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the HTTP server bound by default to TCP port 3465. Insufficient checks on URLs containing paths such as '~root' allows attackers to access arbitrary files in the underlying OS. Accessing configuration files that contain LDAP and database credentials can lead to further compromise.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability.

## Disclosure Timeline

- 2006-12-18 - Vulnerability reported to vendor
- 2007-10-31 - Coordinated public release of advisory
