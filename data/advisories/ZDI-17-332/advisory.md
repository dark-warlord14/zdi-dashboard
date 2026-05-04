# ZDI-17-332: Hewlett Packard Enterprise Network Automation PermissionFilter Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-332
- **ZDI-CAN:** ZDI-CAN-4362
- **Date:** 2017-05-11
- **CVE:** CVE-2017-5812
- **CVSS:** 5.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Network Automation
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-332/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on vulnerable installations of Hewlett Packard Enterprise Network Automation. Authentication is not required to exploit this vulnerability. The specific flaw exists within the PermissionFilter class. This class contains a method that will allow for access to an associated servlet allowing for an attacker to bypass authentication if the URI starts with a specific string. By providing that string, and a directory traversal that follows it, an attacker is able to reach any URI that would map to that servlet without authentication.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: http://h20564.www2.hpe.com/hpsc/doc/public/display?docId=emr_na-hpesbgn03740en_us

## Disclosure Timeline

- 2016-12-15 - Vulnerability reported to vendor
- 2017-05-11 - Coordinated public release of advisory
